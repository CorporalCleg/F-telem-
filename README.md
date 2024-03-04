### 1. Download repo

### 2. Run command:
```
docker build -t fourier .
```
### 3. Put "*.mat" - file to "/fourier/mat_files"

### 4. Run command

```
docker run --rm -it -v $(pwd):/usr/src/fourier fourier python main.py
```