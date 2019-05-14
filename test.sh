#! /bin/bash

dir=vmsd
host=192.168.1.63
user=administrator
passwd=test12#$%

upload(){
	ftp -nv $host  <<-EOF
	user $user $passwd
	binary
	hash
	cd bak
	lcd ~/
	prompt
	mput vmsd.tar.gz
EOF

}

if [ ! -d "./vmsd" ];then
	mkdir $dir
	find /vmfs -name "*.vmsd" -exec cp {} --parents /vmsd/ \;
	tar -zcvf vmsd.tar.gz vmsd
	if [ $? -eq 0 ];then
		upload
		echo "命令执行成功！"
	fi
else
	read -p "该文件夹已存在，是否删除该文件夹[y/n]:" action
	case $action in
	y|Y)
		rm -rf $dir
		if [ $? -eq 0 ];then
			echo -n "文件夹删除成功！"
		fi
		;;
	n|N)
		echo -n "取消删除，退出..."
		exit 0
	esac	
fi
