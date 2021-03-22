YEAR=$(date +"%Y")
if [[ $(find . -type d -iname $YEAR | grep $YEAR) -eq 1 ]]; then
    exit 0;
fi
mkdir $YEAR
for n in {01..23}
do
    mkdir $YEAR/day$n
done
