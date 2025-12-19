all:
	landing_scripts/getCal.py
	python landing_scripts/makeCal.py > index.md
	mamba run -n book_312 NODE_TLS_REJECT_UNAUTHORIZED=0 BASE_URL="/SD312" jupyter-book build --site
	rsync -avz --no-p --chmod=Dg+s,ug+rwX,o=rX _build/html/ ssh.cs.usna.edu:/home/scs/taylor/public_html/SD312 --delete
	chmod a+r -R /home/scs/taylor/public_html/SD312

nogoogle:
	mamba run -n book_312 NODE_TLS_REJECT_UNAUTHORIZED=0 BASE_URL="/SD312" jupyter-book build --site
	rsync -avz --no-p --chmod=Dg+s,ug+rwX,o=rX _build/html/ ssh.cs.usna.edu:/home/scs/taylor/public_html/SD312 --delete
	chmod a+r -R /home/scs/taylor/public_html/SD312
