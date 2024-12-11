<blockquote>
<p>이 문서는 &lt;오브젝트 (조영호 지음)&gt;을 읽으며 작성한 개인 노트입니다.</p>
</blockquote>
<p>객체들의 협력 구조가 다르면 어떤 문제가 발생할까?</p>
<ul>
<li>코드가 이해하기 어렵고,</li>
<li>코드 수정으로 인해 버그가 발생할 위험성이 높아진다</li>
<li>각 협력이 서로 다른 패턴을 따르면, 결국 전체적인 설계가 무너지게 된다</li>
</ul>
<p>또한, 객체지향 패러다임의 장점인 재사용을 활용하기 위해서는 일관성 있는 협력 방식이 필수적이다. </p>
<p><strong>일관성</strong>은 설계에 드는 비용을 감소시킨다.</p>
<ul>
<li>과거의 해결 방법을 반복적으로 사용해서 유사한 기능을 구현하는 데 드는 시간과 노력을 대폭 줄인다</li>
<li>코드가 이해하기 쉬워진다<ul>
<li>문제를 이해하는 것만으로도 코드의 구조를 예상할 수 있다</li>
</ul>
</li>
</ul>
<h1 id="01-핸드폰-과금-시스템-변경하기">01. 핸드폰 과금 시스템 변경하기</h1>
<p>요구사항의 변경을 통해 일관성 있는 협력에 대해 알아보자.</p>
<p>핸드폰 과금 시스템의 요금 정책을 다음과 같이 4가지 방식으로 확장한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/e8b4e38f-78ae-4914-9b0f-c4893615a835/image.png" /></p>
<ol>
<li><strong>고정요금 방식</strong>: 일정 시간 단위로 동일한 요금 부과. 기존의 '일반 요금제'와 동일</li>
<li><strong>시간대별 방식</strong>: 하루 24시간을 특정 시간 구간으로 나눠 각 구간별 요금 부과</li>
<li><strong>요일별 방식</strong>: 요일별로 요금 차등 부과</li>
<li><strong>구간별 방식</strong>: 전체 통화 시간을 일정한 통화 시간에 따라 나눠 구간별 요금 차등 부과. </li>
</ol>
<p>이 새로운 기본 정책을 적용하면 가능한 모든 조합은 다음과 같다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/7ad72a8c-2272-4433-aca2-5248df04be22/image.png" /></p>
<p>요구사항의 변경을 클래스 구조에 반영하면 다음과 같다. </p>
<p>고정요금 방식은 <code>FixedFeePolicy</code>, 시간대별 방식은 <code>TimeOfDayDiscountPolicy</code>, 요일별 방식은 <code>DayOfWeekDiscountPolicy</code>, 구간별 방식은 <code>DurationDiscountPolicy</code>라는 클래스로 구현한다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/86879255-6091-44f9-b48f-5fb23317e3d2/image.png" /></p>
<h3 id="1-고정요금-방식-구현하기">1. 고정요금 방식 구현하기</h3>
<p>고정요금 방식은 기존의 일반요금제와 동일해서 요구사항 변경에 따른 변화는 클래스 이름 변경 뿐이다. 
기존의 <code>RegularPolicy</code> 클래스의 이름을 <code>FixedFeePolicy</code>로 수정하면 된다.</p>
<pre><code class="language-java">public class FixedFeePolicy extends BasicRatePolicy {
    private Money amount;
    private Duration seconds;

    public FixedFeePolicy Money amount, Duration seconds) {
        this. amount = amount;
        this.seconds = seconds;
    }

    @Override
    protected Money calculateCallFee(Call call) {
        return amount.times(call.getDuration).getSeconds) / seconds.getSeconds());
    }</code></pre>
<h3 id="2-시간대별-방식-구현하기">2. 시간대별 방식 구현하기</h3>
<p>시간대별 방식은 통화 기간을 정해진 시간대별로 나누고, 각 시간대별 상이한 계산 규칙을 적용한다. </p>
<p><strong>만약 통화가 여러 날에 걸쳐서 이뤄진다면?</strong>
규칙에 정의된 구간별로 통화를 구분해야 한다. 각 구간에 대해 개별적으로 계산된 요금을 합해야 한다. </p>
<p>정확한 계산을 위해서는 통화의 시작 시간, 종료 시간, 그리고 시작 일자와 종료 일자를 고려해야 하기 때문에 이 기간을 관리할 <code>DateTimeInterval</code> 클래스를 사용한다. </p>
<pre><code class="language-java">public class DateTimeInterval {
    private LocalDateTime from;
    private LocalDateTime to;

    public static DateTimeInterval of(LocalDateTime from, LocalDateTime to) {
        return new DateTimeInterval (from, to);
    }

    public static DateTimeInterval toMidnight(LocalDateTime from) {
        return new DateTimeInterval(
            from,
            LocalDateTime.of(from.toLocalDate(), LocalTime.of(23, 59, 59, 999_999_999)));
    }

    public static DateTimeInterval fromMidnight(LocalDateTime to) {
        return new DateTimeInterval(
            LocalDateTime.of(to. toLocalDate(), LocalTime.of(0, 0),
            to);
    }

    public static DateTimeInterval during(LocalDate date) {
        return new DateTimeInterval(
            LocalDateTime.of(date, LocalTime.of(0, 0)),
            LocalDateTime.of(date, LocalTime.of (23, 59, 59, 999_999_999)));
    }

    private DateTimeInterval(LocalDateTime from, LocalDateTime to) {
        this.from = from;
        this.to = to;
    }

    public Duration duration() {
        return Duration.between(from, to);
    }

    public LocalDateTime getFrom 1
        return from;
    }

    public LocalDateTime getTo) f
        return to;
    }
}</code></pre>
<p>기존의 <code>Call</code> 클래스는 통화 기간을 저장하기 위해 <code>from</code>, <code>to</code>라는 두 개의 <code>LocalDateTime</code> 타입 인스턴스를 포함하고 있었다. </p>
<pre><code class="language-java">public class Call {
    private LocalDateTime from;
    private LocalDateTime to;
}</code></pre>
<p>이제는 기간을 하나의 단위로 표현할 수 있는 <code>DateTimeInterval</code> 타입이 있음으로 <code>from</code>, <code>to</code>를 <code>interval</code>이라는 하나의 인스턴스 변수로 묶을 수 있다. </p>
<pre><code class="language-java">public class Call {

    private DateTimeInterval interval;

    public Call(LocalDateTime from, LocalDateTime to) {
        this.interval = DateTimeInterval.of(from, to);
    }

    public Duration getDuration) {
        return interval.duration();
    }

    public LocalDateTime getFrom() {
        return interval.getFrom();
    }

    public LocalDateTime getTo() {
        return interval.getTo();
    }

    public DateTimelnterval getInterval() {
        return interval;
    }
}</code></pre>
<p>이제 전체 통화 시간을 일자와 시간을 기준으로 분할 계산하자. </p>
<ol>
<li>통화 기간을 일자별로 분리한다.</li>
<li>일자별로 분리된 기간을 다시 시간대별 규칙에 따라 분리하고, 각 기간에 대해 요금을 계산한다. </li>
</ol>
<p>책임을 수행하는 데 필요한 정보를 가장 잘 알고 있는 정보 전문가에 책임을 할당하는 기본 원칙을 따라서 통화 기간을 일자 단위, 시간 단위로 나눠보자.</p>
<h4 id="1-일자-단위">(1) 일자 단위</h4>
<ol>
<li>통화 기간에 대해 가장 잘 알고 있는 객체는 <code>Call</code>이다.</li>
<li>하지만 <code>Call</code>은 기간 자체를 처리하는 방법에 대해서 잘 알지 못한다.</li>
<li>따라서 통화 기간을 일자 단위로 나누는 책임은 <code>DateTimeInterval</code>에게 할당하고, <code>Call</code>이 <code>DateTimeInterval</code>에 분할을 요청하도록 협력을 설계해야 한다. </li>
</ol>
<h4 id="2-시간-단위">(2) 시간 단위</h4>
<p>시간 단위 분할 작업의 정보 전문가는 시간대별 기준을 잘 알고 있는 요금 정책 <code>TimeOfDayDiscountPolicy</code>다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/eb22d7f6-5917-44fa-b026-890ca92e4985/image.png" /></p>
<ol>
<li><code>TimeOfDayDiscountPolicy</code>는 통화 기간을 알고 있는 <code>Call</code>에게 일자별로 통화 기간을 분리할 것을 요청한다.</li>
<li><code>Call</code>은 이 요청을 <code>DateTimeInterval</code>에게 위임한다.</li>
<li><code>DateTimeInterval</code>은 기간을 일자 단위로 분할한 후 분할된 목록을 반환한다.</li>
<li><code>Call</code>은 반환된 목록을 그대로 <code>TimeOfDayDiscountPolicy</code>에 반환한다.</li>
<li><code>TimeOfDayDiscountPolicy</code>는 일자별 기간의 목록을 대상으로 루프를 돌리면서 각 시간대별 기준에 맞는 시작시간(<code>from</code>)과 종료시간(<code>to</code>)를 얻는다.</li>
</ol>
<h4 id="예시">예시</h4>
<ul>
<li>0시부터 19시까지는 10초당 18원의 요금 부과</li>
<li>19시부터 24시까지 10초당 15원의 요금 부과</li>
<li>사용자는 1월 1일 10시부터 1월 3일 15시까지 3일에 걸쳐 통화를 했다</li>
</ul>
<p>과정</p>
<ol>
<li>날짜별로 통화 시간을 분리한다.</li>
<li><code>Call</code>은 기간을 저장하고 있는 <code>DateTimeInterval</code> 타입의 인스턴스 변수인 <code>interval</code>에게 <code>splitByDay</code> 메서드를 호출한다.</li>
<li><code>splitByDay</code> 메서드는 다음 3개 <code>DateTimeInterval</code> 인스턴스를 포함하는 <code>List</code>를 반환한다: <code>1월 1일 10시~24시</code>, <code>1월 2일 0시~24시</code>, <code>1월 3일 0시~15시</code></li>
</ol>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/1e7c5528-5ced-4ae2-a5cd-d5606cc35f5b/image.png" /></p>
<p><code>Call</code>은 이 분리된 <code>List</code>를 시간대별 방식을 위한 <code>TimeOfDayDiscountPolicy</code> 클래스에게 반환하고, <code>TimeOfDayDiscountPolicy</code> 클래스는 일자별로 분리된 각 <code>DateTimeInterval</code> 인스턴스들을 요금 정책에 정의된 각 시간대별로 분할한 후 요금을 부과해야 한다. </p>
<p>예를 들어, 첫 번째 통화 구간인 <code>1월 1일 10시~24시</code>은 시간대별로 나눠야 한다. <code>1월 1일 10시~19시</code>에 해당하는 요금을 부과하고, <code>1월 1일 19시~24시</code>에 해당하는 요금을 부과한다. </p>
<p>이 로직에 기반해 <code>TimeOfDayDiscountPolicy</code> 클래스를 구현한다. </p>
<pre><code class="language-java">public class TimeOfDayDiscountPolicy extends BasicRatePolicy {
    private List&lt;LocalTime&gt; starts = new ArrayList&lt;&gt;();
    private List&lt;LocalTime&gt; ends = new ArrayList&lt;&gt;();
    private List&lt;Duration&gt; durations = new ArrayList&lt;&gt;();
    private List&lt;Money&gt; amounts = new ArrayList&lt;&gt;();
}</code></pre>
<p>각 리스트에서 동일 인덱스를 갖는 요소들이 곧 하나의 규칙을 구성한다. </p>
<h3 id="3-요일별-방식-구현하기">3. 요일별 방식 구현하기</h3>
<p>요일별 방식을 따르면 요일에 따라 요금 규칙을 다르게 설정한다. </p>
<p>시간대별 방식이 구현된 것처럼 4 개의 리스트를 사용할까?</p>
<p>요일별 방식을 개발하는 프로그래머는 규칙을 <code>DayOfWeekDiscountRule</code>이라는 클래스로 구현하는 것이 더 나은 설계라고 판단했다. </p>
<p>이 클래스는 요일의 목록 (<code>dayOfWeeks</code>), 단위 시간 (<code>duration</code>), 단위 요금 (<code>amount</code>)을 인스턴스 변수로 갖는다. </p>
<pre><code class="language-java">public class DayOfWeekDiscountRule {
    private List&lt;DayOfWeek&gt; dayOfWeeks = new ArrayList&lt;&gt;();
    private Duration duration = Duration.ZERO;
    private Money amount = Money. ZERO;

    public Day0fWeekDiscountRule(List&lt;Day0fWeek&gt; dayOfWeeks, Duration duration, Money amount) {
        this.dayOfWeeks = dayOfWeeks;
        this.duration = duration;
        this.amount = amount;
    }

    public Money calculate(DateTimeInterval interval) {
        if (day0fWeeks.contains(interval.getFrom.getDay0fWeek)) {
            return amount.times(interval.duration).getSeconds) / duration.getSeconds);
        }

        return Money.ZERO;
    }
}</code></pre>
<p><code>calculate</code> 메서드는 파라미터로 전달된 <code>interval</code>이 요일 조건을 만족시킨다면 단위 시간과 단위 요금을 이용해 통화 요금을 계산한다.</p>
<p>요일별 방식 또한 통화 기건이 여러 날에 걸쳐있을 수 있고, 시간대별 방식과 같이 기간을 날짜 경계로 분리해야 한다. 이 분리된 통화 기간을 요금별 요금 정책에 따라 계산한다.</p>
<pre><code class="language-java">public class DayOfWeekDiscountPolicy extends BasicRatePolicy {
    private List&lt;DayOfWeekDiscountRule&gt; rules = new ArrayList&lt;&gt;();

    public DayOfWeekDiscountPolicy(List&lt;Day0fWeekDiscountRule&gt; rules) {
        this.rules = rules;
    }

    @Override
    protected Money calculateCallFee(Call call) {
        Money result = Money .ZERO;
        for (DateTimeInterval interval : call.getInterval().splitByDay()) {
            for(DayOfWeekDiscountRule rule: rules) {
                result.plus(rule.calculate(interval));
            }
        }
        return result;
    }
}</code></pre>
<h3 id="4-구간별-방식-구현하기">4. 구간별 방식 구현하기</h3>
<p>여태 구현한 고정요금 방식, 시간대별 방식, 요일별 방식의 구현 클래스를 살펴보면, 각각 클래스는 응집도와 결합도 측면, 로직 구현 면에서도 괜찮아 보인다. 하지만, 이 클래스들 모두가 비슷한 문제를 해결함에도 설계 면에서는 구현 방식이 전혀 다르다.</p>
<p><code>TimeOfDayDiscountPolicy</code>는 각 요소를 저장하는 다수의 리스트를 유지한다.
<code>DayOfWeekDiscountPolicy</code>는 규칙을 구현하는 독립적인 객체를 추가한다.
<code>FixedFeePolicy</code>는 새로운 방식을 고안한다. </p>
<p>우리가 이전에 언급한 일관성에 어긋나는 상황이다. </p>
<p>비일관성은 왜 문제인가?</p>
<ol>
<li>새로운 구현을 추가해야 할 때</li>
<li>기존의 구현을 이해해야 할 때 </li>
</ol>
<p>결론은 유사한 기능은 유사한 방식으로 구현해야 한다는 것이다. 객체지향에서 기능은 객체 간 협력으로 만들어지기 때문에 협력을 일관성있게 만드는 것이 핵심적이다. </p>
<p>그러면 구간별 방식은 어떻게 구현하는가?</p>
<p>이 개발자는 요일별 방식처럼 규칙을 정의하는 새로운 클래스를 추가해서 구현한다. 단, 코드를 재사용하기 위해 <code>FixedFeePolicy</code> 클래스를 상속한다. </p>
<pre><code class="language-java">public class DurationDiscountRule extends FixedFeePolicy {

    private Duration from;
    private Duration to;

    public DurationDiscountRule(Duration from, Duration to, Money amount, Duration seconds) {
        super(amount, seconds);
        this.from = from;
        this.to = to;
    }

    public Money calculate(Call call) {
        if (call.getDuration().compareTo(to) &gt; 0) {
            return Money.ZERO;
        }
        if (call.getDuration().compareTo(from) &lt; 0) {
            return Money.ZERO;
        }

        // 부모 클래스의 calculateFee(phone)은 Phone 클래스 파라미터로 받는다.
        // calculateFee(phone)을 재사용하기 위해
        // 데이터를 전달할 용도로 임시 Phone을 만든다.
        Phone phone = new Phone(null);
        phone.call(new Call(call.getFrom().plus(from),
                    call.getDuration().compareTo(to) &gt; 0 ? call.getFrom).plus(to) : call.getTo()));

        return super.calculateFee(phone);
    }
}</code></pre>
<p>이제 여러 개의 <code>DurationDiscountRule</code>을 이용해 <code>DurationDiscountPolicy</code>를 구현할 수 있다. </p>
<pre><code class="language-java">public class DurationDiscountPolicy extends BasicRatePolicy {
    private List«DurationDiscountRule&gt; rules = new ArrayList&lt;&gt;();

    public DurationDiscountPolicy(List&lt;DurationDiscountRule&gt; rules) {
        this.rules = rules;
    }

    @Override
    protected Money calculateCallFee(Call call) {
        Money result = Money ZERO;
        for(DurationDiscountRule rule: rules) {
            result.plus(rule.calculate(call));
        }
        return result;
    }
}</code></pre>
<p><code>DurationDiscountPolicy</code> 클래스는 할인 요금을 계산하고, 클래스의 단일책임 원칙을 준수하지만, 비슷한 목적을 갖는 타 클래스와 구현 방식이 다르다.</p>
<p>또한, <code>FixedFeePolicy</code>의 서브타입이 아닌<code>DurationDiscountRule</code>이 <code>FixedFeePolicy</code>를 상속하는 것이 옳은 선택이였을까?</p>
<h1 id="02-설계에-일관성-부여하기">02. 설계에 일관성 부여하기</h1>
<p>일관성 있는 설계를 위해서는</p>
<ul>
<li><strong>변하는 개념을 변하지 않는 개념으로부터 분리하라</strong></li>
<li><strong>변하는 개념을 캡슐화하라</strong></li>
</ul>
<pre><code class="language-java">public class ReservationAgency {
    public Reservation reserve(Screening screening, Customer customer, int audienceCount) {
        for(DiscountCondition condition : movie.getDiscountConditions)) {
            if (condition.getType() == DiscountConditionType.PERIOD) {
                // 기간 조건인 경우
            } else {
                // 회차 조건인 경우
            }
        }
        if (discountable) {
            switch(movie.getMovieType)) {
                case AMOUNT_DISCOUNT:
                    // 금액 할인 정책인 경우
                case PERCENT_DISCOUNT:
                    // 비율 할인 정책인 경우
                case NONE_DISCOUNT:
                    // 할인 정책이 없는 경우
            }
        } else {
            // 할인 적용이 불가능한 경우
        }
    }
}</code></pre>
<p>위 코드는 할인 조건의 종류 결정, 할인 정책 결정 로직이 존재한다. 변경의 주기가 다른 코드가 하나의 클래스 내에 공존하기 때문에 새로운 할인 정책, 조건을 추가하기 위해서 기존 코드를 수정해야 하는 불편함이 존재한다. </p>
<p>객체지향적 접근은 조금 다르다. 객체지향에서 변경을 다룰 때는 주로 조건 로직을 객체 간 이동으로 바꾼다. </p>
<pre><code class="language-java">public class Movie {
    private DiscountPolicy discountPolicy;
    public Money calculateMovieFee(Screening screening) {
        return fee.minus(discountPolicy.calculateDiscountAmount(screening));
    }
}</code></pre>
<p>위 코드를 확인하면, <code>Movie</code> 클래스는 현재의 할인 정책이 무엇인지 확인하지 않고, 단순히 현재 할인 정책을 나타내는 <code>discountPolicy</code>에 필요한 전송할 뿐이다. </p>
<p>이런 조건 로직을 객체 간 이동으로 바꾸는 게 객체지향에서 다형성이다.</p>
<h4 id="1-변하는-개념을-변하지-않는-개념으로부터-분리하라">1. 변하는 개념을 변하지 않는 개념으로부터 분리하라</h4>
<p>할인 정책과 할인 조건의 타입을 체크하는 조건문이 개별적인 변경이였다면, 우리는 각 조건문을 개별적인 객체로 분리했다. 이 객체들과 일관성 있게 협력하기 위해서 또 타입 계층을 구성했다.</p>
<h4 id="2-변하는-개념을-캡슐화하라">2. 변하는 개념을 캡슐화하라</h4>
<p><code>Movie</code>는 잘 변하지 않지만, 할인 정책은 자주 변하는 개념이다. <code>Movie</code>로부터 할인 정책을 캡슐화하기 위해 할인 정책을 <code>Movie</code>로부터 분리하고, 추상 클래스인 <code>DiscountPolicy</code>를 부모 삼아 상속 계층을 구성한다. </p>
<p>그래서 <code>Movie</code>가 알고 있는 정보는 협력하는 객체가 단지 <code>DiscountPolicy</code> 클래스의 인터페이스에 정의된 <code>calculateDiscountAmount</code> 메시지를 이해할 수 있다는 것 뿐이다.</p>
<h2 id="캡슐화">캡슐화</h2>
<p>캡슐화는 단순히 data hiding 뿐만 아니라 소프트웨어 안에서 변할 수 있는 모든 개념을 감춰야 한다. </p>
<p>예를 들어 객체의 퍼블릭 인터페이스와 구현을 분리해서 자주 변경되는 내부 구현을 안정적인 퍼블릭 인터페이스 뒤로 숨긴다. </p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/645bebfe-9e9d-4879-9d14-5eec5f7f9c9b/image.png" /></p>
<ul>
<li><strong>데이터 캡슐화</strong>: 인스턴스 변수를 private로 설정한다. 이 속성에 접근할 수 있는 유일한 방법은 메서드를 이용하는 것이다.</li>
<li><strong>메서드 캡슐화</strong>: 클래스 내부와 서브클래스만 접근할 수 있도록 <code>protected</code>로 설정하여 캡슐화한다.</li>
<li><strong>객체 캡슐화</strong>: 객체 인스턴스 변수를 private로 설정한다. 곧 합성이다.</li>
<li><strong>서브타입 캡슐화</strong>: <code>Movie</code>는 <code>DiscountPolicy</code>를 알고 있지만 그의 서브타입, 구현 클래스에 대해서는 알지 못한다. 그럼에도 협력이 가능하다.</li>
</ul>
<p>서브타입 캡슐화와 객체 캡슐화를 적용하려면 </p>
<h4 id="변하는-부분을-분리해서-타입-계층을-만든다">변하는 부분을 분리해서 타입 계층을 만든다.</h4>
<p>변하지 않는 부분으로부터 변하는 부분을 분리한다. </p>
<ul>
<li>변하는 부분들의 공통적인 행동은 추상 클래스나 인터페이스로 추상화한 후, 변하는 부분들이 이 추상 클래스나 인터페이스를 상속받게 한다. </li>
</ul>
<h4 id="변하지-않는-부분의-일부로-타입-계층을-합성한다">변하지 않는 부분의 일부로 타입 계층을 합성한다.</h4>
<p>변하지 않는 부분의 일부로 타입 계층을 합성한다.</p>
<ul>
<li>변하지 않는 부분에서는 변경되는 구체적인 사항에 결합돼서는 안된다.</li>
<li>의존성 주입과 같이 결합도를 느슨하게 유지할 수 있는 방법으로 오직 추상화에만 의존하게 만든다.</li>
</ul>
<h1 id="03-일관성-있는-기본-정책-구현하기">03. 일관성 있는 기본 정책 구현하기</h1>
<h2 id="변경-분리하기">변경 분리하기</h2>
<p>변하는 개념과 변하지 않는 개념을 분리한다.</p>
<p>핸드폰 과금 시스템의 기본 정책에서 변하는 부분과 변하지 않는 부분을 구별한다. </p>
<ul>
<li>기본 정책은 한 개 이상의 규칙으로 구성된다</li>
<li>하나의 규칙은 적용조건과 단위요금의 조합이다. </li>
</ul>
<p>적용 조건의 세부 내용이 변화에 해당한다. 따라서 변하지 않는 규칙으로부터 변하는 적용조건을 분리해야 한다.</p>
<h2 id="변경-캡슐화하기">변경 캡슐화하기</h2>
<p>변경을 캡슐화해서 파급효과를 줄여야 협력을 일관성있게 만들 수 있다. 변경을 캡슐화하는 가장 좋은 방법은 다음과 같다</p>
<ol>
<li>변하지 않는 부분으로부터 변하는 부분을 분리한다</li>
<li>변하는 부분의 공통점을 추상화한다</li>
<li>변하지 않는 부분이 오직 이 추상화에만 의존하도록 관계를 제한한다</li>
</ol>
<p>핸드폰 예시에서 변하지 않는 건 규칙, 변하는 건 적용조건이기 때문에 규칙으로부터 적용조건을 분리해서 추상화한 후 시간대별, 요일별, 구간별 방식을 이 추상화의 서브타입으로 만든다. </p>
<ul>
<li><code>FeeRule</code> - 규칙을 구현하는 클래스<ul>
<li><code>feePerDuration</code> - <code>FeeRule</code>의 인스턴스 변수로 단위요금을 나타낸다</li>
</ul>
</li>
<li><code>FeeCondition</code> - 적용조건을 구현하는 인터페이스<ul>
<li>각 정책별로 달라지는 부분은 서브타입으로 구현</li>
</ul>
</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/9e3e6336-f71f-4cb0-ae1c-b16089c29392/image.png" /></p>
<h2 id="협력-패턴-설계하기">협력 패턴 설계하기</h2>
<p>객체들의 협력 방식을 고민해보자. </p>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/3828cc11-71c7-4ea8-b964-90e6ec7a8081/image.png" /></p>
<p>하나의 요금을 계산하기 위해서는 두 개의 작업이 필요하다.</p>
<ol>
<li>전체 통화 시간을 각 규칙의 적용 조건을 만족하는 구간들로 나누는 것</li>
<li>분리된 통화 구간에 단위요금을 적용해서 요금을 계산하는 것</li>
</ol>
<p>이 두 개의 책임을 객체에 할당하자. </p>
<p>첫 작업은 적용조건을 가장 잘 아는 정보 전문가, <code>FeeCondition</code>에 할당하는 것이 적절하다</p>
<p>두번째에는 요금기준의 정보 전문가인 <code>FeeRule</code>이 가장 적절할 것이다.</p>
<h2 id="추상화-수준에서-협력-패턴-구현하기">추상화 수준에서 협력 패턴 구현하기</h2>
<p>적용조건을 표현하는 추상화인 <code>FeeCondition</code>은 <code>findTimeIntervals</code>, 한 개의 오퍼레이션을 포함하는 인터페이스다. </p>
<pre><code class="language-java">public interface FeeCondition {
    List&lt;DateTimeInterval&gt; findTimeIntervals(Call call);
}</code></pre>
<p><code>FeeRule</code>은 단위요금과 적용조건을 저장하는 두 개의 인스턴스 변수로 구성된다. </p>
<pre><code class="language-java">public class FeeRule {
    private FeeCondition feeCondition;
    private FeePerDuration feePerDuration;
    ...
    public Money calculateFee(Call call) {
        return feeCondition.findTimeIntervals(call)
            .stream()
            .map(each -&gt; feePerDuration.calculate(each))
            .reduce(Money.ZERO, (first, second) -&gt; first.plus(second));
    }
}</code></pre>
<p><code>FeePerDuration</code>은 단위 시간당 요금 개념을 표현한다.</p>
<pre><code class="language-java">public class FeePerDuration {
    private Money fee;
    private Duration duration;

    ...
    public Money calculate(DateTimeInterval interval) {
        return fee.times(Math.ceil((double) interval.duration().toNanos() / duration.toNanos()));
    }
}</code></pre>
<p>이 설계로 <code>BasicRatePolicy</code>는 <code>FeeRule</code>의 컬렉션으로 전체 통화 요금을 계산할 수 있다.</p>
<pre><code class="language-java">public class BasicRatePolicy implements RatePolicy {
    private List&lt;FeeRule&gt; feeRules = new ArrayListO;

    ...
    @Override
    public Money calculateFee(Phone phone) {
        return phone.getCalls()
            .stream()
            .map(call -&gt; calculate(call))
            .reduce(Money ZERO, (first, second) - first.plus(second));
    }
  private Money calculate(Call call) {
      return feeRules.stream()
            .map(rule -&gt; rule.calculateFee(call))
            .reduce(Money.ZERO, (first, second) - first.plus(second));
  }
}</code></pre>
<h3 id="구체적인-협력-구현하기">구체적인 협력 구현하기</h3>
<p>현재의 요금제가 어느 정책인지 결정하는 기준은 <code>FeeCondition</code>을 대체하는 객체의 타입이 무엇인가에 달려있다. 이 말은 곧 <code>FeeCondition</code> 인터페이스를 실체화하는 클래스에 따라 기본 정책의 종류가 달라진다는 의미다. </p>
<p>각 적용조건은 <code>FeeCondition</code>을 구현한다. </p>
<pre><code class="language-java">public class TimeOfDayFeeCondition implements FeeCondition {
    ...
}</code></pre>
<pre><code class="language-java">public class DayOfWeekFeeCondition implements FeeCondition {
    ...
}</code></pre>
<pre><code class="language-java">public class DurationFeeCondition implements FeeCondition {
    ...
}</code></pre>
<p>협력을 일관성있게 만들었기 때문에 변하지 않는 부분은 분리되어 재사용할 수 있다. 또한 새로운 부분을 추가할 때는 변하는 부분만 구현하면 된다. </p>
<p>코드의 재사용성이 향상되고 테스트해야 하는 코드의 양이 감소한다. </p>
<p>유사한 기능에 대해 유사한 협력 패턴을 적용하는 것은 <strong>개념적 무결성</strong>을 유지할 수 있는 효과적인 방법이다. </p>
<h3 id="협력-패턴에-맞추기">협력 패턴에 맞추기</h3>
<p>고정요금 정책만 남았다. 고정요금 정책은 타 정책과 달리 규칙이라는 개념이 필요하지 않고, 단위요금 정보만 있으면 충분하다. </p>
<p>다른 조건이지만, 가급적 기존의 협력 패턴에 맞추는 것이 좋은 방법이다. </p>
<pre><code class="language-java">public class FixedFeeCondition implements FeeCondition {
    @Override
    public List&lt;DateTimeInterval&gt; findTimeIntervals(Call call) {
        return Arrays.asList(call.getInterval());
    }
}</code></pre>
<p><img alt="" src="https://velog.velcdn.com/images/becooq81/post/cc22d9d3-ea15-4ac4-885e-27b0fe8334cd/image.png" /></p>
<h3 id="패턴을-찾아라">패턴을 찾아라</h3>
<p>애플리케이션에서 유사한 기능에 대한 변경이 지속적으로 발생하고 있다면</p>
<ol>
<li>변경을 캡슐화할 수 있는 적절한 추상화를 찾아라</li>
<li>이 추상화에 변하지 않는 공통적인 책임을 할당하라</li>
</ol>