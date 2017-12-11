
Param($IP, $Sub)

echo "IP: $IP"
echo "Subnet: $Sub"

# ネットワークアダプターの情報を格納する変数
$GetNet = Get-NetAdapter 

# 比較する最大のネットワークアダプター数を取得する変数
$end = $GetNet.count
# While 文の作業用変数
$count = 0

while ($count -le $end) {
# 比較用の変数を取得する
    $tmp1 = $count
    $tmp2 = $tmp1 + 1
    if ($GetNet[$tmp1].ifIndex -lt $GetNet[$tmp2].ifIndex) {
        $IfIndex = $GetNet[$tmp1].ifIndex
    }    
    $count++
}