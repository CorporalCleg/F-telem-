### 1. Download repo

### 2. Run command (build container):
```
docker build -t fourier1 .
```
### 3. Put "*.mat" - file to "/fourier/mat_files"

### 4. Run command (run script in container):

```
docker run --rm -v $(pwd):/usr/src/fourier fourier1 python fourier/main.py
```