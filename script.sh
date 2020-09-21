while true
do
   files=$(ls -l | grep "^-" | wc -l)
   folders=$(ls -l | grep ^d | wc -l)

   echo "Contents of custom_tmp: $files files, $folders folders" 
   sleep 10
done
