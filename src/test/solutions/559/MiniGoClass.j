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
	anewarray java/lang/String
	astore_1
.var 1 is a [Ljava/lang/String; from Label2 to Label3
	iconst_3
	anewarray java/lang/String
	dup
	iconst_0
	ldc "apple"
	aastore
	dup
	iconst_1
	ldc "banana"
	aastore
	dup
	iconst_2
	ldc "cherry"
	aastore
	astore_1
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
Label5:
Label9:
	aload_1
	iload_2
	aaload
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iload_2
	iconst_1
	iadd
	istore_2
Label10:
	goto Label4
Label6:
Label3:
Label1:
	return
.limit stack 16
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
