echo "Stopping website service..."
systemctl --user stop website
echo "Discarding local changes..."
git reset --hard
echo "Pulling remote changes..."
git pull
echo "Starting website service..."
systemctl --user start website
echo "Done."
