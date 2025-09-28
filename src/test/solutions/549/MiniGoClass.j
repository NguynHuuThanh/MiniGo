.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static lcm(II)I
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label2:
	iload_0
	iload_1
	imul
	iload_0
	iload_1
	invokestatic MiniGoClass/gcd(II)I
	idiv
	ireturn
Label3:
Label1:
.limit stack 8
.limit locals 2
.end method

.method public static gcd(II)I
Label0:
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label2:
	iload_1
	iconst_0
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	iload_0
	ireturn
Label9:
	goto Label5
Label4:
Label5:
	iload_1
	iload_0
	iload_1
	irem
	invokestatic MiniGoClass/gcd(II)I
	ireturn
Label3:
Label1:
.limit stack 12
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	bipush 12
	bipush 18
	invokestatic MiniGoClass/lcm(II)I
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label2:
Label3:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
