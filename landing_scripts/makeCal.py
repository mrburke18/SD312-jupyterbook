#!/usr/bin/env python3

import csv
import json
import re
import os
from datetime import date, timedelta, datetime, time

def strip_links(text):
    """Remove markdown links, leaving only the visible text."""
    return re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)

def adjust_links_for_subdirectory(text):
    """
    Converts markdown links [Text](url) to HTML <a href="../url">Text</a>
    if the URL is relative.

    [Notes](files/a.pdf) -> <a href="../files/a.pdf">Notes</a>
    """
    def replace_match(match):
        label = match.group(1)
        url = match.group(2)
        # Ignore absolute URLs, absolute paths, or anchors
        if re.match(r'^(https?://|/|#)', url):
            return match.group(0)

        # Return adjusted HTML link with ../ prepended
        return f'<a href="../{url}">{label}</a>'

    # Regex matches standard markdown links: [label](url)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_match, text)

def make_links_root_relative(text):
    """
    Prepends a '/' to relative link paths so they resolve from the project root.
    Ignores existing absolute paths, external URLs, and anchors.
    Example: [Notes](files/lec1.pdf) -> [Notes](/files/lec1.pdf)
    """
    # Matches "](" followed by text that is NOT http(s), /, or #
    return re.sub(r'(\]\()(?!(?:https?://|/|#))', r'\1/', text)

# Define global constants for time
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir,'courseInfo.json'), 'r') as f:
    course_info = json.load(f)

# Set the time class begins from the course info file
CLASS_HOUR, CLASS_MINUTE = course_info.get('time', [0, 0])
CLASS_TIME = time(CLASS_HOUR, CLASS_MINUTE)

# Set the current time when the script is run
CURRENT_DATETIME = datetime.now()

def generate_schedule():
    """
    Generates a course schedule in markdown format, including a list of 
    currently active assignments.
    """
    # 1. Load remaining course information and calendar data
    try:
        calpath = os.path.join(script_dir,'cal.tsv')
        with open(calpath, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader)  # Skip the header row
            cal_data = list(reader)
    except FileNotFoundError as e:
        print(f"Error: Could not find a required file. Make sure '{e.filename}' is in the same directory.")
        return

    # 2. Process course info, holidays, and special schedule days
    year = course_info.get('year', 2025)
    start_month, start_day = course_info.get('start', [1, 1])
    start_date = date(year, start_month, start_day)
    
    day_map = {'M': 0, 'T': 1, 'W': 2, 'R': 3, 'F': 4}
    lecture_days_str = course_info.get('lectures', 'MWF')
    lecture_days = {day_map[char] for char in lecture_days_str}
    
    holidays = {date(year, m, d): name for m, d, name in course_info.get('holidays', [])}
    
    other_events = {}
    for month, day, message in course_info.get('other', []):
        event_date = date(year, month, day)
        if event_date not in other_events:
            other_events[event_date] = []
        other_events[event_date].append(message)

    weird_day_map = {
        date(year, m, d): day_map[day_char] 
        for m, d, day_char in course_info.get('weird', [])
    }

    # 3. Process the TSV data into a structured list of lectures
    lectures = []
    for row in cal_data:
        is_new, notes_text, notes_link, assign_text, assign_link, assign_due = row
        if is_new == 'x':
            lectures.append({'notes': [], 'assignments': []}) # "due" key is removed
        if not lectures: continue

        if notes_text:
            lectures[-1]['notes'].append(f"[{notes_text}]({notes_link})" if notes_link else notes_text)
        if assign_text:
            lectures[-1]['assignments'].append(f"[{assign_text}]({assign_link})" if assign_link else assign_text)
        
        # If a due date exists, format it and append it to the last assignment
        if assign_due and assign_due.strip():
            try:
                parts = assign_due.strip().split()
                if len(parts) == 2:
                    due_month, due_day = map(int, parts)
                    due_year = year if due_month >= start_month else year + 1
                    due_date_obj = date(due_year, due_month, due_day)
                    # Format as: (due Mon 01/11)
                    due_annotation = due_date_obj.strftime("(due %a %m/%d)")
                    if lectures[-1]['assignments']:
                        lectures[-1]['assignments'][-1] += f" {due_annotation}"
            except (ValueError, TypeError):
                continue # Skip if due date is not in the expected format

    # 4. Generate the complete schedule of all events
    schedule_map = {}
    valid_lecture_dates = []
    current_date = start_date
    while len(valid_lecture_dates) < len(lectures):
        if current_date.year > year + 1:
            print("Error: Date generation exceeded one year.")
            break
        
        effective_weekday = weird_day_map.get(current_date, current_date.weekday())
        
        if current_date not in holidays and effective_weekday in lecture_days:
            valid_lecture_dates.append(current_date)
        current_date += timedelta(days=1)
    
    for i, lecture_date in enumerate(valid_lecture_dates):
        info = lectures[i]
        schedule_map[lecture_date] = {
            'notes': "<br>".join(info['notes']),
            'assignment': "<br>".join(info['assignments']),
        }

    all_special_dates = set(holidays.keys()) | set(other_events.keys())
    for event_date in all_special_dates:
        if event_date not in schedule_map:
            schedule_map[event_date] = {'notes': '', 'assignment': ''}
        holiday_msg = f"**{holidays.get(event_date)}** - No Class" if event_date in holidays else ""
        other_msgs = [f"**{m}**" for m in other_events.get(event_date, [])]
        full_message = "<br>".join(filter(None, [holiday_msg] + other_msgs))
        existing_notes = schedule_map[event_date]['notes']
        schedule_map[event_date]['notes'] = f"{existing_notes}<br>{full_message}" if existing_notes and full_message else existing_notes or full_message

    all_events = [{'date': dt, **data} for dt, data in schedule_map.items()]
    all_events.sort(key=lambda x: x['date'])

    # 5. Filter for currently active assignments by parsing the annotation
    active_assignments = []
    for event in all_events:
        if event['assignment']:
            assignments = event['assignment'].split('<br>')
            for assignment_str in assignments:
                match = re.search(r'\(due (\w{3} \d{2}/\d{2})\)', assignment_str)
                if not match:
                    continue
                
                try:
                    due_str_part = match.group(1) # e.g., "Mon 01/11"
                    
                    # Parse date and determine the correct year
                    parsed_dt = datetime.strptime(due_str_part, "%a %m/%d")
                    due_month = parsed_dt.month
                    due_year = year if due_month >= start_month else year + 1
                    due_date_obj = date(due_year, due_month, parsed_dt.day)

                    # Create the time boundaries for the assignment
                    assigned_boundary = datetime.combine(event['date'], CLASS_TIME)
                    due_boundary = datetime.combine(due_date_obj, CLASS_TIME)

                    # Check if the current time is within the active window
                    if assigned_boundary <= CURRENT_DATETIME < due_boundary:
                        active_assignments.append(assignment_str)
                except (ValueError, TypeError, KeyError, IndexError):
                    continue

    # 6. Print the list of active assignments
    if active_assignments:
        print("## Active Assignments")
        for item in active_assignments:
            print(f"* {item}")
        print("\n---")


    # 7. Print the full schedule table (stdout: no links for future dates)
    print("## Full Schedule")
    print("| Date | Notes | Assignment |")
    print("|:---|:---|:---|")
    md_rows = []
    for event in all_events:
        date_str = event['date'].strftime("%a, %b %d")
        is_future = event['date'] > CURRENT_DATETIME.date()

        notes = event['notes']
        assignment = event['assignment']
        if is_future:
            notes = strip_links(notes)
            assignment = strip_links(assignment)
        print(f"| {date_str} | {notes} | {assignment} |")
        # Create root-relative versions specifically for fullCal.md
        fc_notes = adjust_links_for_subdirectory(event['notes'])
        fc_assignment = adjust_links_for_subdirectory(event['assignment'])

        md_rows.append(f"| {date_str} | {fc_notes} | {fc_assignment} |")

    # Write full schedule with links to a file
    output_path = os.path.join(script_dir, "..", "fullCal.md")
    with open(output_path, "w") as f:
        f.write("## Full Schedule\n")
        f.write("| Date | Notes | Assignment |\n")
        f.write("|:---|:---|:---|\n")
        for row in md_rows:
            f.write(row + "\n")

if __name__ == "__main__":
    generate_schedule()
