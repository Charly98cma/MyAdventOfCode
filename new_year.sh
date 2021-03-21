YEAR=$(date +"%Y")
mkdir $YEAR
for n in {01..23}
do
    mkdir $YEAR/day$n
done
