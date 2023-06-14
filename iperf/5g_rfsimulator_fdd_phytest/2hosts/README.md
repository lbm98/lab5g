PC 1 (GNB)
```bash
docker compose up -d
docker ps -a

docker cp rfsim5g-oai-gnb:/opt/oai-gnb/rbconfig.raw rbconfig.raw
docker cp rfsim5g-oai-gnb:/opt/oai-gnb/reconfig.raw reconfig.raw

scp rbconfig.raw lbm@192.168.1.28:~/tmprbconfig.raw

git add rbconfig.raw reconfig.raw
git commit -m 'add config files'
git push
```

PC 2 (UE)
```bash
git pull

```