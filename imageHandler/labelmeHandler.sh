#！ /bin/bash


 dir=`ls /Users/xuejian/Desktop/labelme/json/`

 path="/Users/xuejian/Desktop/labelme/data/"
a=0
cd /Users/xuejian/Desktop/labelme/json/

 for i in $dir
 do
     labelme_json_to_dataset ${dir} -o ${path}${a}_json
     a=$(($a+1))
 done

