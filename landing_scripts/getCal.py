#!/usr/bin/env python3
import os

from newDownload import download_private_sheet_as_tsv

script_dir = os.path.dirname(os.path.abspath(__file__))
cal_path = os.path.join(script_dir,'cal.tsv')
download_private_sheet_as_tsv('https://docs.google.com/spreadsheets/d/1GtaD7DsdIs7t0BYnnsRrxQWtgT-Yd70PU5Sjfsmwmtk/edit',cal_path)
