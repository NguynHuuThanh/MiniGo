.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static x I
.field static y I

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
.var 1 is i I from Label2 to Label3
	bipush 10
	istore_1
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
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
	iload_1
	invokestatic io/putIntLn(I)V
	goto Label6
Label10:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label6:
	iload_1
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 10
.limit locals 3
.end method

.method public static <clinit>()V
Label0:
Label2:
	iconst_5
	putstatic MiniGoClass/x I
	getstatic MiniGoClass/x I
	putstatic MiniGoClass/y I
Label3:
Label1:
	return
.limit stack 1
.limit locals 0
.end method
