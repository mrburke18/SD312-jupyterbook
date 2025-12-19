all:
	landing_scripts/getCal.py
	python landing_scripts/makeCal.py > index.md
	mamba run -n book_312 jupyter-book build .
	rsync -avz --no-p --chmod=Dg+s,ug+rwX,o=rX _build/html/ ssh.cs.usna.edu:/home/scs/taylor/public_html/SD312
	#rsync -avzr book/_build/html/ /home/scs/taylor/public_html/sd311 --delete
	chmod a+r -R /home/scs/taylor/public_html/SD312
