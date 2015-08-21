# Resm
Resm is a simple manager, that allows to control someone's resources.

##Makefile interface
*make build* — prepare Resm<br />
*make clean* — delete all files from prepared project Resm<br />
*make run* — run Resm<br />
*make run_unit* — run tests<br />
*make install* — install Resm as OS service<br />
*make uninstall* — stop and totally remove resm from OS<br />
*make install_depends* — install all the parts of resm for its correct running<br />

##How to work with resm

If you did "make install", now you can manage resm like any other linux service:<br />
*service resm start* - for Ubuntu<br />
*/etc/init.d/resm start* - another Linux pack<br />

If you did only "make build":<br />
*cd build*<br />
*./resm {start|stop|restart|blockedstart}*<br />

*start|stop|restart* — manage Resm, as service<br />
*blockedstart* — run Resm in console-block-mode, press Crtl+C for exit<br />

##Resm configuration
Resm configuration file is *resm.cfg*, you can edit it with any text redactor.

Parameters:<br />
*restport* — set port<br />
*resourcescount* - set max amount of resources<br />

##3-d parts
For auto installation of all the necessary applications and modules type command:<br />
*./install_depends*<br />
If you type command "make install", all the applications and modules will install automatically.
