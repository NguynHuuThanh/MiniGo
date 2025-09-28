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
	iconst_2
	newarray int
	astore_1
.var 1 is a [I from Label2 to Label3
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	astore_1
	iconst_2
	newarray float
	astore_2
.var 2 is b [F from Label2 to Label3
	iconst_0
.var 3 is i I from Label2 to Label3
	iconst_0
	istore_3
Label4:
	iload_3
	iconst_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
Label9:
	aload_2
	iload_3
	aload_1
	iload_3
	iaload
	i2f
	fastore
Label10:
Label5:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label6:
	aload_2
	iconst_1
	faload
	invokestatic io/putFloat(F)V
Label3:
Label1:
	return
.limit stack 25
.limit locals 4
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
