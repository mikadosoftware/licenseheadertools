echo "First doctests"

python licensetoollib.py

echo "next functional testing"

rm -rf test/fodder
cp -r test/examples/ test/fodder
python fileheadermaker.py --conf=conf.ini --fldr=test/fodder
diff test/goodfodder test/fodder

