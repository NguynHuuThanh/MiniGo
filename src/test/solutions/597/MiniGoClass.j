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

.method public static factorial(I)I
Label0:
.var 0 is n I from Label0 to Label1
Label2:
	iload_0
	iconst_1
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	iconst_1
	ireturn
Label9:
	goto Label5
Label4:
Label5:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MiniGoClass/factorial(I)I
	imul
	ireturn
Label3:
Label1:
.limit stack 14
.limit locals 1
.end method

.method public static combination(II)I
Label0:
.var 0 is n I from Label0 to Label1
.var 1 is k I from Label0 to Label1
Label2:
	iload_0
	invokestatic MiniGoClass/factorial(I)I
	iload_1
	invokestatic MiniGoClass/factorial(I)I
	iload_0
	iload_1
	isub
	invokestatic MiniGoClass/factorial(I)I
	imul
	idiv
	ireturn
Label3:
Label1:
.limit stack 11
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_5
	iconst_2
	invokestatic MiniGoClass/combination(II)I
	invokestatic io/putIntLn(I)V
	bipush 10
	iconst_3
	invokestatic MiniGoClass/combination(II)I
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
