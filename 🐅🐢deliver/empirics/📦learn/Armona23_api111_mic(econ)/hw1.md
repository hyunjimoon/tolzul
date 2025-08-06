Alexander Kuptel, Josh Mak, Sarah Baum
1. Lexicographic preference is complete, transitive, strongly monotone

a. 
- Complete: For any two bundles $A$ and $B$, either $A \succ B, B \succ A$, or $A \sim B$.
- Transitive: If $A \succ B$ and $B \succ C$, then $A \succ C$.
- Strongly Monotone: If $A$ has more of at least one good and no less of any other good compared to $B$, then $A \succ B$.
e.g. of monotone but not strongly monotone: Leontief
![[Pasted image 20230914132427.png]]
Proofs:
Completeness:
For any two bundles $A\left(x_1, y_1\right)$ and $B\left(x_2, y_2\right)$ :
1. If $x_1>x_2$, then $A \succ B$.
2. If $x_1<x_2$, then $B \succ A$.
3. If $x_1=x_2$ and $y_1>y_2$, then $A \succ B$.
4. If $x_1=x_2$ and $y_1<y_2$, then $B \succ A$.
5. If $x_1=x_2$ and $y_1=y_2$, then $A \sim B$.
Thus, the preference is complete.

Transitivity:
If $A\left(x_1, y_1\right) \succ B\left(x_2, y_2\right)$, $B\left(x_2, y_2\right) \succ C\left(x_3, y_3\right)$. We can observe four cases for the first element.
1. If $x_1>x_2>x_3$, then $A \succ C$ (by the first criterion).
2. If $x_1=x_2>x_3$ and $y_1>y_2$, then $A \succ C$ (by the first criterion).
3. If $x_1>x_2=x_3$ and $y_2>y_3$, then $A \succ C$ (by the first criterion).
4. If $x_1=x_2=x_3$ and $y_1>y_2>y_3$, then $A \succ C$ (by the second criterion).
Thus, the preference is transitive.

Strongly Monotone:
If $A\left(x_1, y_1\right)$ and $B\left(x_2, y_2\right)$ are such that $x_1 \geq x_2$ and $y_1 \geq y_2$, with at least one inequality being strict.
1. If $x_1>x_2$, then $A \succ B$ (by the first criterion).
2. If $x_1=x_2$ and $y_1>y_2$, then $A \succ B$ (by the second criterion).
Thus, the preference is strongly monotone.
In summary, lexicographic preferences are complete, transitive, and strongly monotone under these conditions.

---
2. monotonic utility representation
 $f($.) is a strictly increasing function, such that $\forall x, y \in \mathbb{R}, x \geq y$ $\Longleftrightarrow \mathrm{f}(\mathrm{x}) \geq \mathrm{f}(\mathrm{y}) . \mathrm{u}($.) is utility function representing $\succsim$, where $\mathrm{x} \succsim \mathrm{y} \Longleftrightarrow$ $\mathrm{u}(\mathrm{x}) \geq \mathrm{u}(\mathrm{y})$. Because $\mathrm{x} \succsim \mathrm{y} \Longleftrightarrow \mathrm{u}(\mathrm{x}) \geq \mathrm{u}(\mathrm{y})$ and, by definition of strict increase $\mathrm{f}(\mathrm{x}) \Longleftrightarrow$ $\mathrm{f}(\mathrm{u}(\mathrm{x})) \geq \mathrm{f}(\mathrm{u}(\mathrm{y}))$, then it follows that $\mathrm{f}(\mathrm{u}(\mathrm{x}))$ also represents $\mathrm{x} \succsim \mathrm{y}$.
---
3. discrete utility representation
a. let U(x) =1 which satisfies rationality (complete and transitive)
b. |X|=N 
suppose there exist a utility function $u(X)$ that is able to differentiate N objects. Meaning w.l.o.g. u(X1) >  ... > u(Xn), then  $X1 \succ X2 .. \succ Xn$ . With one more object z added to the set $X$, regardless of the order of z (wlog.  $X1 \succ X2 .. X_{i} \succ z \succ X_{i+1}.. \succ Xn$ ) we can construct a utility function s.t. ordering of  u(X1) >  u(Xi)> u(z) > u(X_i+1)... > u(Xn) conforms that of preference. To be more specific, using completeness of real numbers, there exist some real number between u(Xi) and u(Xi+1) which we can assign to u(z).

---
4. 
4.a consumers don't burn their money so wealth is 100 * 100 + 100 * 100 = 20000 in year 1 and 12000 + 80c in year 2.

4.b wasp: x1 and x2 are different and if p1 * x(p2, w2) <= w1 then p2 * x(p1,w1) > w2. i.e. 
100 * x(100, 12000 + 80c) <= 20000

120 x 100 + c x 100 <= 100 x 100 + 100 x 100 -> c <= 80
100 x 80 + 100 x 100 <= 120 x 100 + c x 80 -> c >= 75
hence c in [75, 80]


----
(i wonder whether we can solve this with graph)
![[Pasted image 20230914132551.png|300]]

---- 

4.c
since wealth is 18000 in year 3, year 1's bundle is affordable (100 x 100 + 80 x 100 = 18k). let x, y as wheat and coffee of year 3 + assuming warp should be satisfied, 

![[Pasted image 20230919085441.png]]

(1) Constraint on budget
$$
\begin{aligned}
x \cdot 100+y \cdot 80 & =18000 \\
x & =180-0.8 y
\end{aligned}
$$
(2) Constraint based on year 1 preference
$$
\begin{array}{r}
x \cdot 100+y \cdot 100 \leq 100 \cdot 100+100 \cdot 100 \\
100 x+100 y \leq 20000 \\
x+y \leq 200 \\
180-0.8 y+y \leq 200 \\
180+0.2 y \leq 200 \\
0.2 y \leq 20 \\
y \leq 100
\end{array}
$$
(3) Constraint based year 1 preference
$$
\begin{aligned}
100 \cdot 100+100.80 & \leq x \cdot 100+y \cdot 80 \\
10000+8000 & \leq 100 x+80 y \\
18000 & \leq 100 x+80 y \\
1800 & \leq 1 \times+0.8 y \\
180 & \leq 180-0.8 y+0.8 y
\end{aligned}
$$
therefore: $y \leq 100$


![[Pasted image 20230919083536.png]]