<blockquote>
<p>해당 글은 Java 17부터 생겨난 <code>sealed</code>에 대한 Oracle의 공식 문서를 참고하여 작성했습니다.</p>
</blockquote>
<h1 id="sealed-class">Sealed Class</h1>
<p><code>Sealed</code> 키워드는 다른 클래스 또는 인터페이스가 해당 클래스 또는 인터페이스를 상속하거나 구현하는 행위를 제한한다. <code>permits</code> 키워드와 함께 사용하여 해당 클래스 또는 인터페이스를 상속하거나 구현할 수 있는 클래스 또는 인터페이스를 명시한다. </p>
<p>객체지향 프로그래밍의 핵심 개념인 상속, 그리고 상속의 이점인 코드의 재사용에 반하는 개념이기도 하다. 우리가 알고 있는 Java의 객체지향 프로그래밍대로라면, 새로운 클래스를 만들 때 이미 존재하는 클래스 또는 인터페이스를 최대한 활용(상속 또는 구현을 통해)하여 코드 유지보수성과 재사용을 향상하고자 한다. 특히 하나의 클래스에 대한 수정 사항이 이 클래스를 상속하는 타 클래스에도 반영된다는 점이 유지보수 면에서 탁월하다. </p>
<p>그러면 <code>Sealed</code>는 왜 존재하는가? 무슨 용도로 사용하는가?</p>
<h3 id="sealed-class는-언제-사용하는가">Sealed Class는 언제 사용하는가?</h3>
<p>객체지향 프로그래밍의 장점인 상속을 왜 제한하고 싶을까? 제한해서 얻는 이점은 무엇일까?</p>
<p>답은 개발자의 컨트롤에 있다. 상속을 허용한다는 것은 무궁무진한 가능성을 연다는 것과도 같다. 해당 클래스의 개발자는 다른 개발자들이 상속을 통해 클래스의 메서드를 오버라이딩하는 등, 클래스의 변형과 확장을 허용한다.</p>
<p>하지만 개발자가 이를 원하지 않는 경우도 분명 존재한다. 예를 들자면, <code>Math</code>와 같은 라이브러리는 확장 가능성을 열어두는 게 좋을까?</p>
<p>특히 <code>Sealed</code> 키워드는 상속 및 구현을 무조건적으로 막는 것이 아니라, <code>permits</code>을 통해 계층 구조를 허용하기도 하고, 개발자의 입맛에 따라 상속을 제한할 수 있다는 점이 사용하기 편리하다.</p>
<p>그러니까 개발자가 컨트롤할 수 있는 범위 내에서만 확장해야 할 때 또는 하고 싶을 때 활용성이 높다고 볼 수 있다.</p>
<h1 id="sealed-클래스의-선언">Sealed 클래스의 선언</h1>
<p>클래스에 <code>sealed</code> 키워드를 붙이기 위해서는 다음 순서를 따른다</p>
<p>&lt;접근제어자&gt; - <code>sealed class</code> - &lt;클래스명&gt; - <code>extends</code> 및 <code>implements</code> - <code>permits</code> - &lt;허용하는 클래스 목록&gt;</p>
<blockquote>
<p><code>permits</code> 키워드로 허용하는 클래스 목록은 <code>sealed</code> 키워드에 해당하는 클래스를 상속할 수 있다. <code>sealed</code> 클래스를 상속하는 클래스에 대한 조건은 다음 섹션에서 설명한다.</p>
</blockquote>
<p><code>sealed</code> 클래스인 <code>Shape</code>을 상속하는 3개 클래스 <code>Circle</code>, <code>Square</code>, <code>Rectangle</code> 클래스다</p>
<pre><code class="language-java">public sealed class Shape
    permits Circle, Square, Rectangle {
}</code></pre>
<p><code>final</code> 클래스 <code>Circle</code>은 더 이상 상속될 수 없다.</p>
<pre><code class="language-java">public final class Circle extends Shape {
    public float radius;
}</code></pre>
<p><code>non-sealed</code> 클래스 <code>Square</code>은 클래스의 상속을 제한하지도 방지하지도 않는다. <code>Shaped</code> 클래스가 모르는 클래스도 <code>Square</code> 클래스를 상속하여 간접적으로 상속을 허용할 수 있다.</p>
<pre><code class="language-java">public non-sealed class Square extends Shape {
   public double side;
}   </code></pre>
<p><code>sealed</code> 클래스 <code>Rectangle</code>은 <code>Shape</code> 클래스와 마찬가지로 <code>permits</code> 키워드를 통해 자신을 상속할 수 있는 클래스를 명시한다.</p>
<pre><code class="language-java">public sealed class Rectangle extends Shape permits FilledRectangle {
    public double length, width;
}</code></pre>
<blockquote>
<p><code>sealed</code> 클래스가 상속을 허용하는 서브클래스를 같은 파일 내에 정의하면 <code>permits</code> 키워드를 사용할 필요가 없다.</p>
</blockquote>
<pre><code class="language-java">package com.example.geometry;

public sealed class Figure
    // The permits clause has been omitted
    // as its permitted classes have been
    // defined in the same file.
{ }

final class Circle extends Figure {
    float radius;
}
non-sealed class Square extends Figure {
    float side;
}
sealed class Rectangle extends Figure {
    float length, width;
}
final class FilledRectangle extends Rectangle {
    int red, green, blue;
}
</code></pre>
<h3 id="sealed-클래스를-상속하는-클래스에-대한-조건">Sealed 클래스를 상속하는 클래스에 대한 조건</h3>
<p>허용된 서브클래스 (<code>permitted subclass</code>, 키워드는 아니지만, <code>permits</code> 키워드에 기반해서 허용해서 쓰이는 표현이다)는 다음과 같은 조건을 따른다</p>
<ul>
<li>컴파일 시점에 <code>sealed</code> 클래스가 접근할 수 있어야 한다. </li>
<li><code>sealed</code> 클래스를 직접적으로 상속해야 한다. 즉, <code>sealed</code> 클래스를 상속하는 클래스를 상속하는 것은 해당되지 않는다</li>
<li>다음 3가지 제어자 중 단 1가지를 사용해서 <code>sealing</code>을 어떻게 진행할지 명시해야 한다.<ul>
<li>(1) <code>final</code>: 더 이상 상속을 허용하지 않는다</li>
<li>(2) <code>sealed</code>: <code>permits</code>으로 명시한 서브클래스에 대해서만 상속을 허용한다</li>
<li>(3) <code>non-sealed</code>: 어느 서브클래스던 상속을 허용한다. 부모인<code>sealed</code> 클래스는 해당 키워드로 인한 상속을 방지할 수 없다.</li>
</ul>
</li>
<li><code>sealed</code> 클래스와 같은 모듈 내에 존재해야 한다. <code>sealed</code> 클래스가 이름을 명시하지 않은 모듈 내에 존재하면, 같은 패키지 내에 존재해야 한다. </li>
</ul>
<h1 id="sealed-인터페이스의-선언">Sealed 인터페이스의 선언</h1>
<p><code>Sealed</code> 인터페이스도 <code>sealed</code> 클래스와 마찬가지로 <code>sealed</code> 제어자로 선언하면 된다. 다음 순서를 따른다.</p>
<p>&lt;접근제어자&gt; - <code>sealed</code> - &lt;인터페이스명&gt; - <code>extends</code> &lt;확장하는 인터페이스 목록&gt; - <code>permits</code> &lt;구현을 허용하는 클래스 목록 및 확장을 허용하는 인터페이스 목록&gt;</p>
<p>다음은 <code>Expr</code>라는 <code>sealed</code> 인터페이스와 이 인터페이스를 구현할 수 있는 클래스들이다.</p>
<pre><code class="language-java">package com.example.expressions;

public class TestExpressions {
  public static void main(String[] args) {
    // (6 + 7) * -8
    System.out.println(
      new TimesExpr(
        new PlusExpr(new ConstantExpr(6), new ConstantExpr(7)),
        new NegExpr(new ConstantExpr(8))
      ).eval());
   }
}

sealed interface Expr
    permits ConstantExpr, PlusExpr, TimesExpr, NegExpr {
    public int eval();
}

final class ConstantExpr implements Expr {
    int i;
    ConstantExpr(int i) { this.i = i; }
    public int eval() { return i; }
}

final class PlusExpr implements Expr {
    Expr a, b;
    PlusExpr(Expr a, Expr b) { this.a = a; this.b = b; }
    public int eval() { return a.eval() + b.eval(); }
}

final class TimesExpr implements Expr {
    Expr a, b;
    TimesExpr(Expr a, Expr b) { this.a = a; this.b = b; }
    public int eval() { return a.eval() * b.eval(); }
}

final class NegExpr implements Expr {
    Expr e;
    NegExpr(Expr e) { this.e = e; }
    public int eval() { return -e.eval(); }
}</code></pre>
<h1 id="record-클래스도-permit될-수-있을까">Record 클래스도 permit될 수 있을까?</h1>
<p><code>sealed</code> 클래스 및 인터페이스의 <code>permit</code> 표현에 <code>record</code> 클래스도 포함될 수 있을까?</p>
<p><code>record</code> 클래스는 기본적으로 <code>final</code>임을 내포하고 있다. 그래서 허용된 서브클래스의 조건 중 하나인 <code>final</code>, <code>non-sealed</code>, <code>sealed</code> 키워드 중 <code>final</code>을 충족한다 판단되어 키워드 없이도 <code>sealed</code> 클래스를 상속할 수 있다. </p>
<h1 id="sealed-관련-api">Sealed 관련 API</h1>
<p><code>java.lang.Class</code>는 <code>sealed</code> 클래스 및 인터페이스와 관련한 메서드 2개를 가지고 있다.</p>
<ul>
<li><code>java.lang.constant.ClassDesc[] permittedSubclasses()</code> : 해당 클래스가 <code>sealed</code>이라면 해당 클래스의 모든 허용된 서브클래스를 배열에 담아 리턴한다. 해당 클래스가 <code>sealed</code>가 아니라면 빈 배열을 리턴한다.</li>
<li><code>boolean isSealed()</code>: 해당 클래스 또는 인터페이스가 <code>sealed</code>라면 <code>true</code>를 리턴한다. 아니라면 <code>false</code>를 리턴한다.</li>
</ul>
<hr />
<p>출처: <a href="https://docs.oracle.com/en/java/javase/17/language/sealed-classes-and-interfaces.html">오라클</a></p>