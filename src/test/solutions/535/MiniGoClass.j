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
	iconst_5
.var 1 is a I from Label2 to Label3
	iconst_5
	istore_1
	bipush 10
.var 2 is b I from Label2 to Label3
	bipush 10
	istore_2
	iload_1
	iload_2
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	ldc "a > b"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label9:
	goto Label5
Label4:
	iload_1
	iload_2
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	ldc "a == b"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label15:
	goto Label11
Label10:
Label16:
	ldc "a < b"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label17:
Label11:
Label5:
Label3:
Label1:
	return
.limit stack 13
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
