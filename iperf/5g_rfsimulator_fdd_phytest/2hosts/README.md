## Setup

PC 1 (GNB)
```bash
docker compose up -d
docker ps -a

docker cp rfsim5g-oai-gnb:/opt/oai-gnb/rbconfig.raw ../ue/rbconfig.raw
docker cp rfsim5g-oai-gnb:/opt/oai-gnb/reconfig.raw ../ue/reconfig.raw

git add .
git commit -m 'add config files'
git push
```

PC 2 (UE)
```bash
git pull

docker compose up -d
```

## Ping Test

PC 1 (GNB)
```bash
docker exec -it rfsim5g-oai-gnb bash
ping -I -c20 oaitun_enb1 10.0.1.2
```

## Iperf Test

PC 2 (UE)
```bash
docker exec -it rfsim5g-oai-nr-ue bash
iperf -s -i 1 -u -B 10.0.1.2
```

PC 1 (GNB)
```bash
docker exec -it rfsim5g-oai-gnb bash
iperf -c 10.0.1.2 -u -i 1 -t 10 -b 500K --bind 10.0.1.1
```