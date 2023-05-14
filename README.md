# Garbage_Collection

### Q. GC 에 대해 조사하고, 본인의 깃허브에 public 프로젝트로 등록하여 정리하시오.</p>

가비지 컬렉션(Garbage Collection, 이하 GC)은 프로그래밍 언어에서 사용되는 메모리 관리 기법 중 하나입니다. GC는 메모리 누수를 방지하고, 더 이상 필요하지 않은 객체(가비지)를 자동으로 탐지하여 해제하는 작업을 수행합니다. 이를 통해 개발자가 메모리를 명시적으로 관리하지 않아도 됩니다.

GC의 작동 방식은 크게 세 단계로 나눌 수 있습니다. 첫 번째는 Reachability Analysis(도달성 분석)입니다. GC는 root set이라는 메모리 공간을 참조하는지 확인하고, root set에서 시작해 모든 객체를 순회하며 각 객체가 참조하고 있는 다른 객체를 확인합니다. 이렇게 순회하면서 도달할 수 없는 객체를 가비지로 간주합니다.

두 번째 단계는 Mark and Sweep(표시와 정리)입니다. GC는 도달할 수 있는 모든 객체에 표식(mark)을 붙이고, 표식이 없는 객체를 가비지로 처리합니다. 이후 메모리에서 가비지 객체가 차지하고 있는 공간을 해제합니다.

세 번째 단계는 Compact(압축)입니다. 가비지 수집 이후에는 메모리 공간에 불규칙한 구멍이 생길 수 있습니다. 이 공간을 압축하여, 메모리 단편화를 해결합니다.

GC가 제대로 동작하기 위해서는 몇 가지 규칙을 따르는 것이 좋습니다. 첫째, 불필요한 객체는 null로 설정하여 참조하지 않도록 해야합니다. 둘째, 객체가 더 이상 필요하지 않을 때 null로 설정해야합니다. 마지막으로, 대용량 데이터 구조는 작은 단위로 나누어 사용하면 GC의 효율성을 높일 수 있습니다.
  
  </p>

  
### Q. 왜 필요하고, 어떤 매커니즘으로 동작되는지 (본인이 확실히 이해한 내용을 기술)

#### 필요한 이유 </h3>
코딩을 하는 과정에서 메모리 할당과 해제를 제어하는 것은 중요합니다. 메모리 누수(memory leak)는 메모리를 해제하지 않은 상태로 프로그램이 종료됨으로써 메모리 공간이 계속 쌓이게 되어 시스템에 치명적인 영향을 끼칠 수 있습니다.

메모리를 수동으로 할당하고 해제하는 것은 매우 어려울 뿐만 아니라 코드의 길이도 증가합니다. 따라서, 가비지 컬렉션은 개발자가 메모리 관리를 수동으로 할 필요 없이, 자동으로 더 이상 사용하지 않는 메모리를 해제해줍니다. 이를 통해 개발자는 더 간단하고 효율적인 코드를 작성할 수 있습니다.

또한, 가비지 컬렉션은 메모리 해제 문제로 인한 버그를 줄이는 효과도 있습니다. 메모리 관리는 복잡한 작업 중 하나이며, 실수할 가능성이 높습니다. 가비지 컬렉션을 사용하면 개발자는 이러한 실수를 방지할 수 있습니다.

마지막으로, 가비지 컬렉션은 성능을 향상시키는 데 도움이 됩니다. 개발자가 메모리를 수동으로 해제하는 방식은 효율적이지 않을 수 있습니다. 가비지 컬렉션은 시스템의 사용 가능한 메모리를 최대한 활용하여 프로그램의 성능을 개선합니다.

###  매커니즘
##### 파이썬은 자동으로 메모리가 부족한 경우 가비지 컬렉션을 실행합니다. </p> 또한, 파이썬의 가비지 컬렉션 모듈 gc를 이용해 수동으로 가비지 컬렉션을 실행할 수도 있습니다. </p>마지막으로gc.collect() 메소드를 호출하여 가비지 컬렉션을 직접 실행할 수 있습니다.
------------------------------------------------------------------
#### 파이썬에서의 GC (언어마다 다름)
##### 참조 횟수 기반 GC
객체가 생성될 때마다 참조 카운트를 두고, 해당 객체를 참조하는 변수나 객체의 수가 0이 되면 메모리에서 자동으로 삭제하는 방식입니다. 
하지만 순환 참조가 발생하면 참조 카운트가 0이 되지 않아 메모리 누수가 발생할 수 있습니다. 이를 해결하기 위해 파이썬은 쓰레기 수집 기능을 추가로 제공합니다.

##### 쓰레기 수집 기능
참조 횟수 기반 GC로 처리할 수 없는 순환 참조같은 경우를 메모리 누수로부터 해제할 수 있도록 해줍니다. 
파이썬의 쓰레기 수집 기능은 대부분 참조 횟수 기반 GC와 다른 스레드에서 실행되는 쓰레기 수집기에 의해 처리됩니다.





## Q. GC 가 제대로 동작되도록 코드를 어떻게 작성해야 하는지, 어떻게 하면 GC 로도 메모리 leak 이 발생되는지 예제 코드와 함께 설명

#### File Name : Leak.py, solveLeak.py
#### File Contents : Memory leak를 일으키는 경우와 해결법 

------------------------------------------------------------------

#### File Name : TeskLeak.py
#### File Contents : GC 로도 Memory leak이 발생하는 경우와 제대로 동작되도록 코드를 어떻게 작성해야지 서술
------------------------------------------------------------------


##### ★★해당 레파지토리에 올려놨습니다.★★
