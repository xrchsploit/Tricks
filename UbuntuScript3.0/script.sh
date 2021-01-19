#Disclaimer

echo "Please ensure you did: sudo bash script.sh !"

sudo modprobe -n -v cramfs | grep -v mtd

sudo modprobe -n -v freevxfs

sudo modprobe -n -v jffs2 | grep -v mtd

modprobe -n -v hfs
# disables hfsplus, filesystem type
modprobe -n -v hfsplus
#Disables squashfs filesystem
modprobe --showconfig | grep squashfs
# Disables like dvd drives
modprobe -n -v udf | grep -v crc-itu-t

# Disabling USB support and UEFI
grep -E -i '\svfat\s' /etc/fstab
modprobe --showconfig | grep vfat

