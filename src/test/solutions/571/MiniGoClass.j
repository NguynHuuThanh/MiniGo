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

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_3
	newarray int
	astore_1
.var 1 is a [I from Label2 to Label3
	iconst_0
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
Label4:
	iload_2
	iconst_3
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
Label9:
	aload_1
	iload_2
	iload_2
	iconst_1
	iadd
	bipush 10
	imul
	iastore
Label10:
Label5:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label6:
	aload_1
	iconst_2
	iaload
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 26
.limit locals 3
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
