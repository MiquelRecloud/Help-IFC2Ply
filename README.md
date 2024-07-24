1. To convert the IFC to obj:
```
docker build -t ifcconvert-env .
docker run --rm -v /mnt/path/to/file:/mnt ifcconvert-env /mnt/K24LC201.ifc /mnt/K24LC201.obj
docker run --rm -v /mnt/path/to/file:/mnt ifcconvert-env /mnt/K24AC201.ifc /mnt/K24AC201_blp.obj --building-local-placement
docker run --rm -v /mnt/path/to/file:/mnt ifcconvert-env /mnt/K24AC201.ifc /mnt/K24AC201_cm.obj --center-model
docker run --rm -v /mnt/path/to/file:/mnt ifcconvert-env /mnt/K24AC201_not_geo.ifc /mnt/K24AC201_not_geo.obj
```

2. To convert the obj to ply:
```
python .\mesh_to_ply.py
```