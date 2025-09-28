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

.method public static bubbleSort([I)V
Label0:
.var 0 is a [I from Label0 to Label1
Label2:
	iconst_0
.var 1 is i I from Label2 to Label3
	iconst_0
	istore_1
Label4:
	iload_1
	iconst_2
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
Label9:
	iconst_0
.var 2 is j I from Label9 to Label10
	iconst_0
	istore_2
Label11:
	iload_2
	iconst_2
	iload_1
	isub
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label13
Label16:
	aload_0
	iload_2
	iaload
	aload_0
	iload_2
	iconst_1
	iadd
	iaload
	if_icmple Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label18
Label22:
.var 3 is temp I from Label22 to Label23
	istore_3
	aload_0
	iload_2
	aload_0
	iload_2
	iconst_1
	iadd
	iaload
	iastore
	aload_0
	iload_2
	iconst_1
	iadd
	iload_3
	iastore
Label23:
	goto Label19
Label18:
Label19:
Label17:
Label12:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label11
Label13:
Label10:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label6:
Label3:
Label1:
	return
.limit stack 52
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	iconst_3
	newarray int
	astore_1
.var 1 is a [I from Label2 to Label3
	iconst_3
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	astore_1
	aload_1
	invokestatic MiniGoClass/bubbleSort([I)V
	aload_1
	iconst_0
	iaload
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
