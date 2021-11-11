systemctl --user stop website
git reset --hard
git pull
systemctl --user start website
