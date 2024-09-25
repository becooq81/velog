<h1 id="스레드">스레드</h1>
<p>스레드는 프로세스 수행의 병렬 처리를 가능케 하는 경량 작업 단위입니다. 하나의 프로세스의 커다란 작업을 여러 스레드에 나눠 처리하여 성능을 높일 수 있죠. </p>
<p>하나의 프로세스 내의 여러 스레드는 각자 독립적인 스택 공간을 가지지만, 나머지 힙, 코드, 데이터 영역은 포인터로 프로세스의 공간을 가르킵니다. 그래서 완전히 독립적인 공간을 갖는 프로세스의 생성과 컨텍스트 스위칭에 비해서는 낮은 비용 덕에 작업 처리의 효율성을 높였습니다.  </p>
<p>스레드는 크게 커널에서 관리하는 커널 레벨 스레드(KLT, Kernel-Level Thread)와 사용자 프로그램에서 관리하는 유저 레벨 스레드(ULT, User-Level Thread)로 구분할 수 있습니다. 커널에서 관리되는 작업이므로, 커널 레벨 스레드는 상대적으로 더 큰 오버헤드를 수반합니다.</p>
<p>커널 레벨 스레드를 생성, 삭제 및 관리하기 위해서는 시스템 콜을 사용해야 하며, 이는 커널 공간으로의 모드 전환과 유저 공간으로의 복귀를 동반합니다. 이러한 모드 스위칭은 컨텍스트 스위칭의 오버헤드를 발생시키며, 생성과 삭제 과정에서도 시스템 콜이 필요해 번거롭습니다.</p>
<p>커널 수준의 컨텍스트 스위칭은 스레드의 컨텍스트뿐만 아니라 레지스터와 프로세서의 전체 컨텍스트도 전환하게 됩니다. 또한, 커널에서 운영되는 스레드이기 때문에 하드웨어 자원에 직접적으로 제한을 받으며, 운영체제에 대한 의존성이 큽니다.</p>
<h1 id="java-thread">Java Thread</h1>
<p>Java의 전통적인 Java Thread는 커널 레벨 스레드입니다. 즉, JVM 내에서 스레드를 생성하면 Java Native Interface (JNI)를 통해 커널 스레드와 매핑됩니다. </p>
<blockquote>
<p>JNI는 OS가 바로 읽을 수 있는 형태의 네이티브 코드 (C, C++ 등) 을 JVM이 호출할 수 있게끔 해주는 인터페이스입니다. JVM은 JNI를 사용하여 별도의 인터프리터 없이도 C/C++로 작성된 코드를 실행할 수 있습니다.  </p>
</blockquote>
<p>스레드 섹션에서 다룬 커널 스레드의 단점인 컨텍스트 스위칭 오버헤드, 운영체제 자원으로 제한되는 커널 스레드 생성 등이 바로 Java 스레드의 단점으로도 이어지죠.</p>
<p>Java 스레드가 개발되는 당시에는 운영체제의 효율성을 최대 끌어내고자 한 구현이였으나, 하드웨어와 운영체제의 성능이 많이 발전한 현재로서는 비효율적인 방식이죠.</p>
<h3 id="java-thread의-구현">Java Thread의 구현</h3>
<p>Java는 <code>java.util.concurrent.ExecutorService</code>로 JVM 내부에서 스레드를 관리하고 실행합니다. <code>ThredPoolExecutor</code>라는 ExecutorService로 실제 스레드를 실행시키고는 하는데, 스레드를 추가할 여유가 있는지 확인한 후 실행하는 <code>Thread.start</code> 메서드에서 <code>synchronized</code>하게 JNI 메서드 <code>start0</code>을 호출하는 과정을 확인할 수 있습니다.</p>
<pre><code class="language-java">java.lang.Thread.java

private native void start0();

public void start() {
    synchronized (this) {
        // zero status corresponds to state &quot;NEW&quot;.
        if (holder.threadStatus != 0)
            throw new IllegalThreadStateException();
        start0();
    }
}</code></pre>
<p>JDK 21을 기준으로 <code>start0</code> JNI 메서드는 다음과 같이 구현되어 있습니다.</p>
<pre><code class="language-java">static JNINativeMethod methods[] = {  
    {&quot;start0&quot;,           &quot;()V&quot;,        (void *)&amp;JVM_StartThread},
    {&quot;setPriority0&quot;,     &quot;(I)V&quot;,       (void *)&amp;JVM_SetThreadPriority},</code></pre>
<p><code>start0</code>에 해당하는 <code>JVM_StartThread</code>는 <code>Thread</code>를 상속하는 <code>JavaThread</code> 클래스 타입 객체를 생성합니다.</p>
<pre><code class="language-java">JVM_ENTRY(void, JVM_StartThread(JNIEnv* env, jobject jthread))  
...
      native_thread = new JavaThread(&amp;thread_entry, sz);
...
JVM_END  

...
class JavaThread: public Thread {  
  friend class VMStructs;
  friend class JVMCIVMStructs;
  friend class WhiteBox;
}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/70557493-afbf-4cd0-bdd0-d7431fcf57ed/image.png" />
출처: 네이버 D2</p>
<p>그래서 스케쥴링은 Java에서 실행되고, 실제 생성/실행 등은 JNI를 통한 시스템 콜로 커널에서 진행되어 JVM의 Heap 공간에 존재하는 여러 유저 레벨 스레드 중 몇몇 스레드가 JVM의 스케쥴링에 의해 커널 스레드와 1:1 매핑됩니다. </p>
<h4 id="tdlr">TDLR;</h4>
<ul>
<li>Java에서 스레드를 생성하면 JNI로 커널 스레드를 생성함</li>
<li>Java의 유저 레벨 스레드가 스케쥴링에 의해 선정되면 커널 스레드와 1:1 매핑됨</li>
</ul>
<h1 id="java-21의-virtual-thread-vt">Java 21의 Virtual Thread (VT)</h1>
<p>커널 레벨 스레드와 1:1 매핑하여 사용한 Java의 전통적인 스레드도 프로세스보다는 효율적이였지만, 요청량이 급격하게 증가하는 서버 환경에서 thread per request를 구현하는 Java MVC 환경에는 충분하지 않았습니다. </p>
<p>각 스레드가 1MB만 차지한다고 가정해도 4GB 메모리 환경은 약 4,000 개의 스레드만을 가질 수 있어서 스레드의 수가 메모리에 의해 크게 제한됩니다. 더 많은 요청을 더 효율적으로 구현해야 하는 문제를 해결하기 위해 Java의 Virtual Thread(VT, 가상 스레드)가 탄생했습니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/62e1f87c-9ff1-4543-9bf5-448787afae0c/image.png" />
출처: 우아한기술블로그</p>
<p>기존의 스레드 모델은 유저 레벨 스레드가 스케쥴링되어 커널 레벨 스레드에 매핑되었다면, 이제는 가상 스레드가 스케쥴링되어 플랫폼 스레드에 매핑됩니다. </p>
<h2 id="java-virtual-thread의-구조">Java Virtual Thread의 구조</h2>
<p>그래서 가상스레드, 플랫폼 스레드, 그리고 <code>ForkJoinPool</code>의 구조를 확인해봅시다.</p>
<blockquote>
<p><code>ForkJoinPool</code>은 분할 정복과 work stealing 방식으로 작업 처리 효율성을 높입니다. 분할 정복은 큰 규모의 작업이 작아질 때까지 재귀적으로 분할하여 동시 처리함을 의미하며, work stealing은 유휴 덱(작업큐)이 바쁜 덱의 끝에서 작업을 가져가서 처리함을 의미합니다. </p>
</blockquote>
<pre><code class="language-java">ForkJoinPool commonPool = ForkJoinPool.commonPool(); // ForkJoinPool에 public static 키워드 붙인 것과 같은 의미
ForkJoinPool forkJoinPool = PoolUtil.forkJoinPool;</code></pre>
<p>런타임의 Virtual Thread를 확인하면 다음과 같은 요소를 확인할 수 있습니다. </p>
<ol>
<li><code>carrierThread</code> : 자신의 작업 큐에서 작업을 가져와 실제 수행까지 처리하는 플랫폼 스레드를 의미합니다. 가상 스레드는 필요에 따라 서로 다른 <code>carrierThread</code>에 마운트되거나 언마운트됩니다. </li>
<li><code>scheduler</code> : <code>ForkJoinPool</code>로, 플랫폼 스레드에 대한 풀 역할을 수행하고, 가상 스레드를 스케쥴링합니다.</li>
<li><code>runContinuation</code> : 가상 스레드의 실제 작업 내용을 가집니다. 가상 스레드의 <code>Continuation</code> 객체는 가상 스레드의 현재 상태를 저장하여 콜 스택, 지역 변수 등을 포함합니다. </li>
</ol>
<p>이 모든 요소들을 활용해 Java의 Virtual Thread가 동작합니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/84df9984-2525-43a8-9e25-2f943102d8da/image.png" />
출처: 우아한기술블로그</p>
<ol>
<li>실행될 가상 스레드의 작업, 즉 <code>runContinuation</code>을 플랫폼 스레드의 작업 큐에 추가(push)합니다.</li>
<li><code>ForkJoinPool</code>이 각 작업 큐의 작업(<code>runContinuation</code>)을 work stealing 방식으로 관리합니다. </li>
<li>작업들은 인터럽트 (I/O, 슬립 등) 또는 완료 시 작업 큐에서 pop되어 힙 메모리로 돌아갑니다. </li>
</ol>
<p>이 과정 중 작업 큐에 작업이 추가되는 과정을 <code>unpark</code>, 작업 큐에서 제거되는 과정을 <code>park</code>라고도 합니다.</p>
<h3 id="unpark">unpark</h3>
<p><code>unpark</code>로 가상 스레드를 플랫폼 스레드에 마운트하여 실행합니다. </p>
<p>다음은 JDK21에서 구현된 가상 스레드에 대한 <code>unpark()</code> 메서드입니다. </p>
<pre><code class="language-java">@Override
@ChangesCurrentThread
void unpark() {
    Thread currentThread = Thread.currentThread();
    if (!getAndSetParkPermit(true) &amp;&amp; currentThread != this) {
        int s = state();
        if (s == PARKED &amp;&amp; compareAndSetState(PARKED, RUNNABLE)) {
            if (currentThread instanceof VirtualThread vthread) {
                vthread.switchToCarrierThread();
                try {
                    submitRunContinuation();
                } finally {
                    switchToVirtualThread(vthread);
                }
            } else {
                submitRunContinuation();
            }
        } else if (s == PINNED) {
            // unpark carrier thread when pinned.
            synchronized (carrierThreadAccessLock()) {
                Thread carrier = carrierThread;
                if (carrier != null &amp;&amp; state() == PINNED) {
                    U.unpark(carrier);
                }
            }
        }
    }
}</code></pre>
<h4 id="1-스레드에게-park-permit을-부여합니다">1. 스레드에게 park permit을 부여합니다.</h4>
<p><code>getAndSetParkPermit(boolean newValue)</code>로 park permit을 설정합니다.</p>
<p>park permit은 스레드가 작업 수행을 계속할 수 있는 권한을 부여하는 boolean 플래그입니다. <code>true</code>면 스레드를 수행할 수 있고, <code>false</code>면 다시 permit을 얻을 때까지 스레드는 중지합니다. </p>
<pre><code class="language-java">private boolean getAndSetParkPermit(boolean newValue) {
    if (parkPermit != newValue) {
        return U.getAndSetBoolean(this, PARK_PERMIT, newValue);
    } else {
        return newValue;
    }
}</code></pre>
<p>해당 메서드는 새롭게 받은 플래그가 기존 플래그와 다른 경우 스레드의 플래그를 업데이트합니다. </p>
<blockquote>
<p>이 때 사용되는<code>Unsafe</code> 클래스의 <code>getAndSetBoolean</code> 메서드가 원자연산인 <code>getAndSetByte</code>을 활용하기 때문에 park permit을 사용하는 메서드 또한 동기화가 보장됩니다.</p>
</blockquote>
<pre><code class="language-java">@ForceInline
public final boolean getAndSetBoolean(Object o, long offset, boolean newValue) {
    return byte2bool(getAndSetByte(o, offset, bool2byte(newValue)));
}</code></pre>
<p>이미 running 중인 스레드는 <code>true</code>를 리턴하고 메서드 수행을 끝내지만, (1) 수행되고 있지 않은, (2) 현재 수행 중인 스레드와 다른 스레드면 컨텍스트 스위칭 작업을 수행합니다. </p>
<h4 id="2-1-우선-현재-수행-중인-스레드의-상태를-확인합니다">2-1. 우선 현재 수행 중인 스레드의 상태를 확인합니다.</h4>
<p><code>int s = state()</code>으로 스레드의 현재 상태를 확인합니다. </p>
<p>스레드가 <code>PARKED</code> 상태면 현재 정지된 스레드로, 재개되길 대기하고 있음을 의미합니다. </p>
<blockquote>
<p>이외에도 <code>RUNNABLE</code>, <code>NEW</code>, <code>WAITING</code>, <code>TERMINATED</code>와 같은 상태를 가질 수 있습니다.</p>
</blockquote>
<p>이후 <code>compareAndSetState</code> 메서드로 현재 스레드의 상태를 <code>PARKED</code>에서 <code>RUNNABLE</code>로 변경합니다. 이를 원자연산으로 수행하여 동시에 스레드들의 상태가 변경되어 경합상태가 발생할 가능성을 방지합니다. </p>
<p>성공적으로 스레드의 상태를 변경했다면 다음 단계로 넘어갑니다.</p>
<h4 id="2-2-현재-스레드가-가상-스레드라면-carrierthread로-스위치하여-작업을-forkjoinpool에-제출합니다">2-2. 현재 스레드가 가상 스레드라면 carrierThread로 스위치하여 작업을 ForkJoinPool에 제출합니다.</h4>
<p>현재 스레드가 가상 스레드인지 확인하고 <code>carrierThread</code>로 스위치합니다.</p>
<pre><code class="language-java">if (currentThread instanceof VirtualThread vthread) {
    vthread.switchToCarrierThread();
}</code></pre>
<blockquote>
<p>가상 스레드는 CPU에 의해 직접적으로 수행되지는 않기 때문에 <code>carrierThread</code>를 통해 작업을 해야 합니다. 가상 스레드와 <code>carrierThread</code>를 분리하는 구조가 작업의 실제 수행과 작업의 논리적인 상태와 흐름 또한 분리하고, 여러 가상 스레드를 필요에 따라 적은 수의 <code>carrierThread</code>에 마운트하고 언마운트해서 제한적인 운영체제 자원을 효율적으로 사용합니다. </p>
</blockquote>
<p><code>submitRunContinuation</code> 메서드를 수행하여 (주로) <code>ForkJoinPool</code> 타입의 <code>Executor</code> 인스턴스에 스레드의 <code>runContinuation</code> 작업을 제출합니다. 이 작업은 큐에 추가되어 수행될 것입니다. </p>
<p>이 작업이 완료되면 다시 가상 스레드로 스위치합니다. </p>
<p>물론 현재 스레드가 가상 스레드가 아니라면 이런 과정을 거칠 필요 없이 바로 스케쥴러에 작업을 제출할 수 있죠. </p>
<h4 id="3-1-현재-스레드의-상태가-pinned라면-carrierthread를-unpark해야-합니다">3-1. 현재 스레드의 상태가 PINNED라면 carrierThread를 unpark해야 합니다.</h4>
<pre><code class="language-java">else if (s == PINNED) {
    // unpark carrier thread when pinned.
    synchronized (carrierThreadAccessLock()) {
        Thread carrier = carrierThread;
        if (carrier != null &amp;&amp; state() == PINNED) {
            U.unpark(carrier);
        }
    }
}</code></pre>
<p>가상 스레드가 <code>synchronized</code> 블록 또는 메서드에 해당하는 코드를 수행하거나, JNI를 통해 네이티브 메서드를 사용하면 플랫폼 스레드(<code>carrierThread</code>)에 <code>PINNED</code>된 상태입니다. </p>
<p><code>PINNED</code>된 가상 스레드의 수행은 특정 플랫폼 스레드에 묶여있기 때문에 이 플랫폼 스레드부터 <code>unpark</code>해줘야 가상 스레드도 수행할 수 있습니다. </p>
<p><code>thread-safe</code>하게 <code>carrierThread</code>를 사용하기 위해 <code>synchronized</code> 키워드로 <code>carrierThreadAccessLock()</code> 메서드를 호출합니다. </p>
<p><code>carrierThread</code>에 NULL 체크를 수행하고, 가상 스레드의 현재 상태가 <code>PINNED</code>임을 다시 확인한 다음 플랫폼 스레드에 대해 <code>unpark</code>을 수행합니다. </p>
<h3 id="park">Park</h3>
<p><code>unpark</code>을 통해 스레드 수행을 재개했다면, <code>park</code>을 통해 스레드를 중지합니다. </p>
<pre><code class="language-java">@Override
void park() {
    assert Thread.currentThread() == this;

    // complete immediately if parking permit available or interrupted
    if (getAndSetParkPermit(false) || interrupted)
        return;

    // park the thread
    boolean yielded = false;
    setState(PARKING);
    try {
        yielded = yieldContinuation();  // may throw
    } finally {
        assert (Thread.currentThread() == this) &amp;&amp; (yielded == (state() == RUNNING));
        if (!yielded) {
            assert state() == PARKING;
            setState(RUNNING);
        }
    }

    // park on the carrier thread when pinned
    if (!yielded) {
        parkOnCarrierThread(false, 0);
    }
}</code></pre>
<h4 id="1-park-메서드를-호출한-스레드가-현재-가상-스레드-인스턴스와-일치하는지-확인합니다">1. <code>park</code> 메서드를 호출한 스레드가 현재 가상 스레드 인스턴스와 일치하는지 확인합니다.</h4>
<p>이 확인 절차를 통해 메서드의 잘못된 사용을 방지합니다. </p>
<h4 id="2-현재-스레드가-park-permit이-있는지-인터럽트되었는지-확인합니다">2. 현재 스레드가 park permit이 있는지, 인터럽트되었는지 확인합니다.</h4>
<p>원자연산 <code>getAndSetParkPermit(false)</code>로 <code>park permit</code> 플래그를 확인합니다. 리턴 값이 <code>true</code>면 <code>park permit</code> 플래그가 <code>true</code>라는 뜻인데, 해당 스레드가 계속 수행될 권한을 가지고 있기 때문에 중지시키면 안된다고 판단하고 메서드를 퇴장합니다.</p>
<p>또한, 인터럽트된 스레드는 즉각적인 처리를 필요로 하기 때문에 <code>park</code>되지 않습니다. </p>
<h4 id="3-이제-park-과정을-시작합니다">3. 이제 park 과정을 시작합니다.</h4>
<p><code>boolean yield</code> 변수를 <code>false</code>로 초기화합니다. <code>park</code> 과정이 성공적으로 수행되어 작업이 안전하게 중지되었으면 이 값이 <code>true</code>로 설정될 것입니다.</p>
<h4 id="3-1-현재-스레드의-상태를-parking로-설정합니다">3-1. 현재 스레드의 상태를 PARKING로 설정합니다.</h4>
<p><code>PARKING</code> 상태는 현재 스레드가 중지되는 과정에 있음을 의미합니다. </p>
<h4 id="3-2-현재-스레드의-작업을-정지합니다">3-2. 현재 스레드의 작업을 정지합니다.</h4>
<p><code>yieldContinuation()</code> 메서드를 수행하여 경량 작업 정지를 시도합니다. 이는 곧 가상 스레드의 컨텍스트 스위칭을 의미하는데, 해당 가상 스레드의 <code>Continuation</code> 객체를 힙에 저장하여 다시 스케쥴링될 때까지 대기 상태로 만드는 과정입니다.
중지에 성공하면 가상 스레드는 플랫폼 스레드에서 언마운트되어 플랫폼 스레드는 다른 작업을 수행할 수 있습니다. </p>
<p>아래는 <code>yieldContinuation</code>의 구현 코드입니다. <code>unmount</code> 메서드를 호출하여 가상 스레드를 플랫폼 스레드에서 언마운트한 후, 가상 스레드의 <code>Continuation</code> 객체를 <code>yield</code>합니다. 이 과정은 일반적인 스레드의 컨텍스트 스위칭과 유사하게, 가상 스레드의 현 상태를 힙에 저장하고, 이전 상태를 복구합니다. </p>
<pre><code class="language-java">@Hidden
@ChangesCurrentThread
private boolean yieldContinuation() {
    // unmount
    notifyJvmtiUnmount(/*hide*/true);
    unmount();
    try {
        return Continuation.yield(VTHREAD_SCOPE);
    } finally {
        // re-mount
        mount();
        notifyJvmtiMount(/*hide*/false);
    }
}</code></pre>
<p><code>unmount</code> 메서드 내에서는 <code>synchronized</code> 키워드로 안전하게 가상스레드를 해제합니다.</p>
<pre><code class="language-java">@ChangesCurrentThread
@ReservedStackAccess
private void unmount() {
    // set Thread.currentThread() to return the platform thread
    Thread carrier = this.carrierThread;
    carrier.setCurrentThread(carrier);

    // break connection to carrier thread, synchronized with interrupt
    synchronized (interruptLock) {
        setCarrierThread(null);
    }
    carrier.clearInterrupt();
}</code></pre>
<p>이 정지 과정의 성공 여부는 <code>yielded</code> 변수에 저장하고, 이 값이 가상 스레드의 상태를 정확하게 반영하는지 확인합니다. </p>
<p>정지에 실패했다면 (<code>!yielded</code>) 스레드의 상태를 <code>PARKING</code>에서 <code>RUNNING</code>으로 되돌리고, 이는 스레드가 계속해서 수행됨을 의미합니다.</p>
<h4 id="3-3-정지에-실패했으면-플랫폼-스레드를-park합니다">3-3. 정지에 실패했으면, 플랫폼 스레드를 park합니다.</h4>
<pre><code class="language-java">// park on the carrier thread when pinned
if (!yielded) {
    parkOnCarrierThread(false, 0);
}</code></pre>
<p>정지가 정상적으로 이루어지지 않았다면 가상 스레드가 플랫폼 스레드에 <code>PINNED</code>되었을 가능성을 의미합니다. </p>
<p>그래서 가상스레드를 <code>park</code>하려고 플랫폼 스레드(<code>carrierThread</code>)를 <code>park</code>합니다.</p>
<h3 id="io에-의한-park-과정은">I/O에 의한 park 과정은?</h3>
<p><code>park(FileDescriptor fd, int event, long nanos)</code>는 해당 파일 디스크립터가 읽기 쓰기 등 특정 이벤트를 위해 준비될 때까지 (또는 특정 대기 시간 동안) 스레드가 스케쥴되지 않도록 합니다.</p>
<pre><code class="language-java">private void park(FileDescriptor fd, int event, long nanos) throws IOException {
    Thread t = Thread.currentThread();
    if (t.isVirtual()) {
        Poller.poll(fdVal(fd), event, nanos, this::isOpen);
        if (t.isInterrupted()) {
            throw new InterruptedIOException();
        }
    } else {
        long millis;
        if (nanos == 0) {
            millis = -1;
        } else {
            millis = NANOSECONDS.toMillis(nanos);
            if (nanos &gt; MILLISECONDS.toNanos(millis)) {
                // Round up any excess nanos to the nearest millisecond to
                // avoid parking for less than requested.
                millis++;
            }
        }
        Net.poll(fd, event, millis);
    }
}</code></pre>
<p>눈 여겨볼 점은, 스레드가 가상 스레드면 <code>poll(int fd, int event, long nanos)</code>를 호출하고, 가상 스레드가 아니면 <code>poll(FileDescriptor fd, int event, long nanos)</code>를 호출합니다. </p>
<p>첫번째는 일반 메서드로 처리하는 반면에 두번째는 네이티브 메서드로 처리합니다. 네이티브 메서드보다는 JVM 내에서 처리하는 과정이 더 효율적이고, 가상 스레드의 장점이기도 하죠. </p>
<h3 id="기존-스레드-모델과의-비교">기존 스레드 모델과의 비교</h3>
<p>JDK 17에서는 <code>park</code>, <code>unpark</code> 개념을 <code>LockSupport.class</code>를 통해 네이티브 메서드로 구현했습니다. JDK 21에서는 가상 스레드의 경우에는 가상 스레드 기반 컨텍스트 스위칭을 진행하는 로직을 추가하여 해당 경우에는 더 가벼운 가상 스레드 기반 컨텍스트 스위칭을 구현합니다. </p>
<p>슬립, I/O에 의한 <code>park</code>/<code>unpark</code> 등도 JDK 17의 네이티브 기반 로직에 가상 스레드를 처리하는 로직을 추가했습니다.</p>
<h1 id="java에서-스레드와-가상-스레드의-성능-비교">Java에서 스레드와 가상 스레드의 성능 비교</h1>
<p>(출처: 네이버 D2)</p>
<blockquote>
<pre><code class="language-yml">server:  
  tomcat:
    threads:
      max: 1</code></pre>
</blockquote>
<pre><code>위처럼 application.yml로 톰캣의 최대 스레드 수를 제한할 수 있습니다.

Spring MVC Tomcat 환경에서 각각 커널 스레드의 수를 1로 제한한 일반 스레드와 가상 스레드에 100개의 호출을 수행해 보면, 일반 스레드는 거의 동시성을 보장할 수 없습니다. 요청와 스레드 간 1:1, 스레드와 커널 스레드 간 1:1 관계이기 때문에 최대 1000ms * 100의 시간이 걸립니다.

하지만 가상 스레드를 사용한다면 거의 동시에 발생하는 100개의 호출을 논블록킹 방식으로 처리하여 커널 스레드 하나만으로도 최대 처리 시간이 약 1000ms입니다. 

I/O와 슬립 등으로 인한 `park`/`unpark` 메서드가 가상 스레드에 관해서는 가상 스레드 수준 스위칭을 제공하는 점을 확인하면 놀랍지 않은 성능 차이죠.

## CPU-bound 작업에서 가상 스레드의 한계

결국 가상 스레드가 수행되기 위해서는 플랫폼 스레드에 마운트되어야 하기 때문에 CPU-Bound 작업에서는 가상 스레드 스위칭이 아닌 플랫폼 스레드 스위칭이 발생합니다. 

이런 상황에서 가상 스레드를 사용하면 플랫폼 스레드 사용 비용과 함께 가상 스레드이 생성 및 스케쥴링 비용까지 추가되어 성능 낭비가 발생합니다. 

# Java Virtual Thread 사용 시 유의사항

오라클에서 직접 가상 스레드 사용 시 유의사항을 발표했습니다.

### 1. 가상 스레드를 Pool하지 마세요.

Java 스레드는 매번 요청이 발생할 때마다 스레드를 생성하고 삭제하는 비용을 절감하기 위해 [pool](https://velog.io/@becooq81/%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C-ThreadPool-Monitor-Fork-Join), 즉 미리 스레드를 만들어두고 필요에 따라 작업에 할당하여 처리합니다. 

스레드는 운영체제에 의해 개수가 제한적인 자원이기 때문에 최대한 효율적으로 활용하는 것이 관건이지만, 가상 스레드는 단순히 애플리케이션 수준의 도메인 객체와도 같습니다. 그렇기 때문에 동시에 처리해야 하는 각 작업당 가상 스레드를 한 개 씩 할당해야 가상 스레드의 이점을 잘 활용할 수 있습니다. 즉, 작은 단위의 작업에도 가상 스레드를 별도로 만들어서 사용해야 합니다. 

최소 10,000개 이상의 가상 스레드를 항상 사용해야 애플리케이션이 가상 스레드의 장점을 잘 활용한다고 볼 수 있습니다. 

### 2. 동시성을 제한해야 하면 세마포어를 사용하세요.

### 3. synchronized 키워드 등으로 인한 Pinning 구간을 지양하세요.

`synchronized` 블록 내의 가상 스레드의 블록킹(blocking) 연산은 곧 플랫폼 스레드, 이어서 커널 스레드의 블락을 유발합니다. 이 상태를 pinning이라 하는데, 소중한 커널 스레드가 블락된 시간이 길어지면 성능 저하로 이어지죠. 

이는 가상 스레드 내에서 `parallelStream`, 네이티브 메서드 등을 사용할 때도 해당됩니다.

이 문제에 대해 해결방안으로 `ReentrantLock`

### 4. ThreadLocal 변수에 재사용 가능한 객체를 캐쉬하지 마세요.

가상 스레드도 일반 스레드처럼 thread-local 변수를 지원합니다. Thread-local 변수는 주로 현재 트랜잭션, 사용자 ID 등 컨텍스트에 엮인 정보를 저장합니다. 이런 사용은 가상 스레드의 목적과도 부합하지만, 문제는 thread-local 변수에 재사용 가능 객체를 캐쉬할 때입니다.

객체의 캐쉬는 여러 스레드가 해당 객체를 공유하고 재사용할 때 의미 있지만, 가상 스레드는 pool되지 않고, 재사용되지 않습니다.

# 마치며

대량 트랜잭션 처리를 위해 종종 Java보다 경량 스레드를 잘 지원하는 Go 언어를 선택하곤 했습니다. `goroutine`은 가볍고 사용이 간편하다는 장점이 있지만, Java로 개발된 시스템과의 융합이 까다롭고, Go의 Stop the World GC 문제를 무시하기 어렵습니다. Java의 가상 스레드는 동기화 등 아직 발전이 필요한 부분이 있지만, 경량 스레드의 필요성을 공식적으로 인정하고 이를 제공하는 것은 언어의 발전 방향을 잘 제시하고 있다고 생각합니다.

- - - 
- [OpenJDK JDK 21 소스 코드](https://github.com/openjdk/jdk21)
- [Oracle 공식 문서 가상 스레드](https://docs.oracle.com/en/java/javase/21/core/virtual-threads.html#GUID-8AEDDBE6-F783-4D77-8786-AC5A79F517C0)
- [GeeksForGeeks 운영체제의 커널 수준 스레드](https://www.geeksforgeeks.org/kernel-level-threads-in-operating-system/)
- [우아한기술블로그 Java의 미래, Virtual Thread](https://techblog.woowahan.com/15398/)
- [카카오페이 테크 [Project Loom] Virtual Thread에 봄(Spring)은 왔는가](https://tech.kakaopay.com/post/ro-spring-virtual-thread/)
- [네이버 D2 Virtual Thread의 기본 개념 이해하기](https://d2.naver.com/helloworld/1203723)</code></pre>