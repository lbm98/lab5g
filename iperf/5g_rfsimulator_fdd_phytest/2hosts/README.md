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