## mkdir ~/.config/fish
## ~/.config/fish/config.fish

#set DIR (cd (dirname (status -f)); and pwd) 
#source $DIR/alias
source $HOME/.bash_cfg/alias
source $HOME/.bash_cfg/alias_cmd

switch "$HOSTNAME"
  case 'localhost'
    # Termux用の設定
    set prompt_color '#FFF450' ## lemon_yellow
    ;;
  case 'raspberry' 'raspi'
    # Raspi用の設定
    set prompt_color '#FF00FF' ## magent
    #set prompt_color '#956DAF' ## purple
    ;;
  case 'deskmini' 'cfnx3'
    # Manjaro用の設定
    set prompt_color '#33CC99' ## Nile_green
    #set prompt_color '#00B379' ## emerald green
    ;;
  case '*'
    # それ以外の設定
    set prompt_color '#90D7EC' ## sky_blue
    ;;
end



# Fish git prompt
set __fish_git_prompt_showdirtystate 'yes'
set __fish_git_prompt_showstashstate 'yes'
set __fish_git_prompt_showuntrackedfiles 'yes'
set __fish_git_prompt_showupstream 'yes'
set __fish_git_prompt_color_branch yellow
set __fish_git_prompt_color_upstream_ahead green
set __fish_git_prompt_color_upstream_behind red
 

# Status Chars
set __fish_git_prompt_char_dirtystate 'Dirt'
set __fish_git_prompt_char_stagedstate 'Added'
set __fish_git_prompt_char_untrackedfiles 'Untrack'
set __fish_git_prompt_char_stashstate 'Stash'
set __fish_git_prompt_char_upstream_ahead ' Commited+'
set __fish_git_prompt_char_upstream_behind ' Commited-'

function fish_prompt --description 'Write out the prompt, prepending the Debian chroot environment if present'    # Set variable identifying the chroot you work in (used in the prompt below)
    if not set -q debian_chroot
        and test -r /etc/debian_chroot
        set debian_chroot (cat /etc/debian_chroot)
    end
    if not set -q __fish_debian_chroot_prompt
        and set -q debian_chroot
        and test -n "$debian_chroot"
        set -g __fish_debian_chroot_prompt "($debian_chroot)"
    end

    # Prepend the chroot environment if present
    if set -q __fish_debian_chroot_prompt
        echo -n -s (set_color yellow) "$__fish_debian_chroot_prompt" (set_color normal) ' '
    end

    switch "$USER"
        case root toor
            echo -n -s "$USER" @ (prompt_hostname) ' ' (set -q fish_color_cwd_root
                                                        and set_color $fish_color_cwd_root
                                                        or set_color $fish_color_cwd) (prompt_pwd)
            echo ''
            echo (set_color normal) '# '

        case '*'
            echo -n -s (set_color $prompt_color) '[' "$USER" @ (prompt_hostname) ':' (prompt_pwd) ']' (__fish_git_prompt)
            echo ''
            echo (set_color normal) '$ '

    end
end
