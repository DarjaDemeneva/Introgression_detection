# !/bin/bash 

grep "Archaic" *.decoded.hap*.txt | awk -F'\t' '$6 > 0.9' | awk 'BEGINS{FS=OFS="\t"} {$3 = $3+1000; print}' > CHS.archaic.decoded.txt

awk '{ sub(/^[^:]*:/, "chr", $1); print $1, $2, $3 }' CHS.archaic.decoded.txt > CHS.archaic.bedGraph.txt

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
' CHS.archaic.bedGraph.txt > CHS.archaic.bedGraph.freq.txt

grep "chr22" CHS.archaic.bedGraph.freq.txt > CHS.chr22.bedGraph.txt
