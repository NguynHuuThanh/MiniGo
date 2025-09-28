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
	bipush 10
	newarray int
	astore_1
.var 1 is arr [I from Label2 to Label3
	bipush 10
	newarray int
	dup
	iconst_0
	bipush 10
	iastore
	dup
	iconst_1
	bipush 20
	iastore
	dup
	iconst_2
	bipush 30
	iastore
	dup
	iconst_3
	bipush 40
	iastore
	dup
	iconst_4
	bipush 50
	iastore
	dup
	iconst_5
	bipush 60
	iastore
	dup
	bipush 6
	bipush 70
	iastore
	dup
	bipush 7
	bipush 80
	iastore
	dup
	bipush 8
	bipush 90
	iastore
	dup
	bipush 9
	bipush 100
	iastore
	astore_1
	iconst_0
.var 2 is sum I from Label2 to Label3
	iconst_0
	istore_2
	iconst_0
.var 3 is i I from Label2 to Label3
	iconst_0
	istore_3
Label4:
	iload_3
	bipush 10
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label6
Label5:
Label9:
	iload_3
	iconst_2
	irem
	iconst_0
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	iload_2
	aload_1
	iload_3
	iaload
	iadd
	istore_2
Label16:
	goto Label12
Label11:
Label17:
	iload_2
	aload_1
	iload_3
	iaload
	isub
	istore_2
Label18:
Label12:
	iload_3
	iconst_1
	iadd
	istore_3
Label10:
	goto Label4
Label6:
	iload_2
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 33
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
