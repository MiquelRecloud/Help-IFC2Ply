1. To convert the IFC to obj:
```
docker build -t ifcconvert-env .
docker run --rm -v /mnt/path/to/file:/mnt ifcconvert-env /mnt/K24LC201.ifc /mnt/K24LC201.obj
```

2. To convert the obj to ply:
```
python .\mesh_to_ply.py
```