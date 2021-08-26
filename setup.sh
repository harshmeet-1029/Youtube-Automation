clear
figlet Mr.venom
read -ep "\e[1;33m Do you want to continue installing IP-Changer \e[0m [y/n]: " answer

if [ $answer = "y" ] || [ $answer = "Y" ]
then
	apt-get install dirmngr apt-transport-https
	apt-key adv --keyserver keyserver.ubuntu.com --recv-key FDC247B7
	sh -c "echo 'deb https://repo.windscribe.com/debian buster main' > /etc/apt/sources.list.d/windscribe-repo.list"
	apt-get update
	apt-get install windscribe-cli
	exit 
elif [ $answer = "n" ] || [ $answer = "N" ]
then
	echo "Ok Byee byee...!!!"
	exit
else
	echo "Can't understand that... Exiting bye bye"
	exit
fi
