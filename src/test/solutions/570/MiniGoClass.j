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

.method public static countOccurrences([II)I
Label0:
.var 0 is arr [I from Label0 to Label1
.var 1 is target I from Label0 to Label1
Label2:
	iconst_0
.var 2 is count I from Label2 to Label3
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
	aload_0
	iload_3
	iaload
	iload_1
	if_icmpne Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	iload_2
	iconst_1
	iadd
	istore_2
Label16:
	goto Label12
Label11:
Label12:
	iload_3
	iconst_1
	iadd
	istore_3
Label10:
	goto Label4
Label6:
	iload_2
	ireturn
Label3:
Label1:
.limit stack 22
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label2:
	bipush 10
	newarray int
	astore_1
.var 1 is a [I from Label2 to Label3
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_2
	iastore
	dup
	iconst_4
	iconst_4
	iastore
	dup
	iconst_5
	iconst_2
	iastore
	dup
	bipush 6
	iconst_5
	iastore
	dup
	bipush 7
	iconst_2
	iastore
	dup
	bipush 8
	bipush 6
	iastore
	dup
	bipush 9
	iconst_2
	iastore
	astore_1
	aload_1
	iconst_2
	invokestatic MiniGoClass/countOccurrences([II)I
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
