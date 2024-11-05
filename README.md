ДЛЯ ЗАПУСКА СНАЧАЛА 

```bash
pip install -r r.txt
g++ -fPIC -shared -o libtestpp.so test.cpp    
uvicorn main:app --reload  
```
