#!/bin/bash

# File containing the lists
input_file="input.txt"

# Read the file and separate the values into left and right lists
left_list=($(awk '{print $1}' "$input_file"))
right_list=($(awk '{print $2}' "$input_file"))

# Sort the lists
sorted_left=($(printf "%s\n" "${left_list[@]}" | sort -n))
sorted_right=($(printf "%s\n" "${right_list[@]}" | sort -n))

# Calculate the total distance
total_distance=0

for i in "${!sorted_left[@]}"; do
  distance=$(( ${sorted_left[i]} > ${sorted_right[i]} ? ${sorted_left[i]} - ${sorted_right[i]} : ${sorted_right[i]} - ${sorted_left[i]} ))
  total_distance=$((total_distance + distance))
done

echo "Total distance: $total_distance"
