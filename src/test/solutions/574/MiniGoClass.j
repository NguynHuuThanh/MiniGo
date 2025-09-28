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

.method public static sumArray([II)I
Label0:
.var 0 is a [I from Label0 to Label1
.var 1 is index I from Label0 to Label1
Label2:
	iload_1
	iconst_2
	if_icmplt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	iconst_0
	ireturn
Label9:
	goto Label5
Label4:
Label5:
	aload_0
	iload_1
	iaload
	aload_0
	iload_1
	iconst_1
	iadd
	invokestatic MiniGoClass/sumArray([II)I
	iadd
	ireturn
Label3:
Label1:
.limit stack 16
.limit locals 2
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
	iconst_5
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	astore_1
	aload_1
	iconst_0
	invokestatic MiniGoClass/sumArray([II)I
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 2
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
