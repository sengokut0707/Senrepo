## . ~/Git_dir/Systems/bash_cfg.bash

script_dir="${HOME}/.bash_cfg"

export alias_bin=${script_dir}/alias_bin
source ${script_dir}/alias
source ${script_dir}/alias_cmd

PATH=$PATH:$HOME/.local/bin
PATH=$PATH:$HOME/Git_dir/Python
PATH=$PATH:$HOME/Git_dir/Ruby
PATH=$PATH:$HOME/Git_dir/Scripts
PATH=$PATH:$HOME/Git_dir/Notes

if type hostname 1>/dev/null 2>/dev/null; then
    HOSTNAME=`hostname`
elif [ -f /etc/hostname ]; then
    HOSTNAME=`cat /etc/hostname`
elif type hostnamectl 1>/dev/null 2>/dev/null; then
    HOSTNAME=`hostnamectl | grep hostname | sed -e 's/Static hostname: //g'`
else
    HOSTNAME=''
fi
export HOSTNAME

case ${HOSTNAME} in
  localhost )
    # Termux用の設定
    PATH=$PATH:$HOME/Git_dir/Termux.cfg/
    PS1='\[\e[1;33m\][\u@\h:\w]\n\$ \[\e[m\]'
    ;;
  raspberry | raspi )
    # Raspi用の設定
    PATH=$PATH:$HOME/Git_dir/Raspi.cfg/
    PS1='\[\e[1;35m\][\u@\h:\w]\n\$ \[\e[m\]'
    ;;
  deskmini )
    # Manjaro用の設定
    PS1='\[\e[1;36m\][\u@\h:\w]\n\$ \[\e[m\]'
    ;;
  cfnx3 )
    # Manjaro用の設定
    PS1='\[\e[1;37m\][\u@\h:\w]\n\$ \[\e[m\]'
    ;;
  * )
    # それ以外の設定
    PS1='\[\e[1;32m\][\u@\h:\w]\n\$ \[\e[m\]'
    ;;
esac

export EDITOR='/usr/bin/vim'

# fishがあれば起動
type fish > /dev/null 2>&1
if [ $? -eq 0 ] ; then
    exec fish
fi
