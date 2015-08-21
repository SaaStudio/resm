build:
	mkdir build
	cp src/*.py build/
	mkdir build/rest
	cp src/rest/*.py build/rest
	cp src/db.sqlite3 build/
	cp src/resm_default.cfg build/resm.cfg
	cd build && python3 resm.py migrate
	cp src/bash/resm_manager build/resm
	chmod +x build/resm

clean:
	rm -r build

run: build
	cd build && python3 resm.py

run_unit: build
	cd build && screen -S resm -d -m python3 resm.py
	echo "Wait 5 second before tests. Rest service starting..."
	sleep 5
	cd build && python3 unit.py
	screen -X -S resm quit

install: build install_depends
	mkdir /usr/lib/resm
	mv build/* /usr/lib/resm
	cp src/bash/resm_init /etc/init.d/resm
	chmod +x /etc/init.d/resm

uninstall:
	/etc/init.d/resm stop
	rm /etc/init.d/resm	
	rm -r /usr/lib/resm

install_depends2:
	apt-get install --yes screen
	chmod -R 777 /var/run/screen
	apt-get install --yes python3 python3-pip
	pip3 install django
	pip3 install djangorestframework"


