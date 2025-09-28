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
	ldc "Hello"
.var 1 is str1 Ljava/lang/String; from Label2 to Label3
	ldc "Hello"
	astore_1
	ldc "World"
.var 2 is str2 Ljava/lang/String; from Label2 to Label3
	ldc "World"
	astore_2
	aload_1
	ldc " "
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_2
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	ldc "Hello"
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/putBoolLn(Z)V
	aload_1
	aload_2
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifeq Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	invokestatic io/putBoolLn(Z)V
	aload_1
	aload_2
	invokevirtual java/lang/String/compareTo(Ljava/lang/String;)I
	ifge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBoolLn(Z)V
Label3:
Label1:
	return
.limit stack 20
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
