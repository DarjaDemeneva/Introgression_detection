# !/bin/bash 

awk 'BEGIN{FS=OFS='\t'}; {$3 = $3+1000; print}' *.decoded.hap*.txt > GBR.decoded.txt # will that change my input files? dont want that to happen 

awk '{ sub(/^[^:]*:/, "chr", $1); print $1, $2, $3 }' GBR.decoded.txt > GBR.archaic.bedGraph.txt

awk '
    {
        # Use the first three columns as the key to track fragment frequency
        key = $1 "\t" $2 "\t" $3

        # Check if the fragment is encountered for the first time
        if (!(key in frequency)) {
            frequency[key] = 1
        } else {
            # Increment the frequency for the current fragment in the array
            frequency[key]++
        }
    }
    END {
        # Print the data with the new column showing the fragment frequency
        for (key in frequency) {
            print key, frequency[key]
        }
    }
' GBR.archaic.bedGraph.txt > GBR.archaic.bedGraph.freq.txt

grep "chr22" GBR.archaic.bedGraph.txt > GBR.chr22.bedGraph.txt