# pytest  [링크](https://docs.pytest.org/en/7.1.x/index.html)
[유튜브](https://youtu.be/cHYq1MRoyI0?t=983)
```bash  
# bash shell  
pip install pytest  
```
- 사용한 버전  
$ python --version  
Python 3.12.1  
```diff
Package   Version
--------- -------
colorama  0.4.6
iniconfig 2.0.0
packaging 23.2
pip       24.0
pluggy    1.4.0
pytest    8.1.0
```

```python  
main\
│
├── source\
│   └── my_functions.py     # 테스트 해야하는 파일
│
└── tests\
    └── conftest.py    # pytest 설정파일
    └── test_01.py     # 기본 예제  
    └── test_02.py     # 테스트 성공했을때
    └── test_03.py     # 테스트 실패했을때
```


`conftest.py` 파일은 pytest 테스팅 프레임워크에서 사용하는 특별한 설정 파일입니다. 이 파일은 pytest가 테스트를 수행하기 전에 자동으로 인식하고 실행하는 코드를 포함하고 있어, 테스트 환경을 설정하거나 공통적으로 사용할 픽스처(fixture)를 정의하는 등의 용도로 사용됩니다.

위의 `conftest.py` 코드는 Python의 모듈 검색 경로(`sys.path`)를 동적으로 조정하는 예시를 보여줍니다. 코드 설명은 다음과 같습니다:

1. **모듈 임포트**: 
   - `sys` 모듈을 임포트하여 Python의 내장 기능과 설정에 접근할 수 있습니다. 특히 `sys.path`는 Python이 모듈을 찾을 때 참조하는 경로 목록입니다.
   - `os` 모듈을 임포트하여 운영 체제의 파일 시스템과 상호작용할 수 있습니다. 이를 통해 경로 조작과 관련된 작업을 수행할 수 있습니다.

2. **`sys.path` 조정**:
   - `os.path.abspath` 함수를 사용하여, `conftest.py` 파일이 위치한 디렉토리의 상위 디렉토리에 있는 `source` 디렉토리의 절대 경로를 구합니다. 이 절대 경로는 플랫폼에 관계없이 일관된 형태로 제공됩니다.
   - `sys.path.insert(0, 경로)`를 호출하여, 구한 `source` 디렉토리의 경로를 `sys.path`의 가장 앞쪽에 추가합니다. 이로써, Python이 모듈을 찾을 때 `source` 디렉토리를 가장 먼저 검색하게 됩니다.

이러한 설정을 통해, `source` 디렉토리에 위치한 Python 모듈을 테스트 코드에서 바로 임포트하여 사용할 수 있게 됩니다. 예를 들어, `source` 디렉토리 안에 `my_module.py`라는 모듈이 있을 경우, 테스트 파일에서 `import my_module`과 같이 직접 임포트하여 사용할 수 있습니다.

`conftest.py` 파일을 사용하는 것은 테스트 환경을 설정하고, 여러 테스트 파일 간에 코드를 재사용할 수 있게 하는 효율적인 방법입니다.