/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.9
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

package org.doubango.ultimateCreditCard.Sdk;

public class ultimateCreditCardSdkJNI {

  static {
    System.loadLibrary("ultimateCreditCard_SDK");
  }

  public final static native long new_UltCreditCardSdkResult__SWIG_0(int jarg1, String jarg2, String jarg3, long jarg4);
  public final static native long new_UltCreditCardSdkResult__SWIG_1(int jarg1, String jarg2, String jarg3);
  public final static native void delete_UltCreditCardSdkResult(long jarg1);
  public final static native int UltCreditCardSdkResult_code(long jarg1, UltCreditCardSdkResult jarg1_);
  public final static native String UltCreditCardSdkResult_phrase(long jarg1, UltCreditCardSdkResult jarg1_);
  public final static native String UltCreditCardSdkResult_json(long jarg1, UltCreditCardSdkResult jarg1_);
  public final static native long UltCreditCardSdkResult_numCards(long jarg1, UltCreditCardSdkResult jarg1_);
  public final static native boolean UltCreditCardSdkResult_isOK(long jarg1, UltCreditCardSdkResult jarg1_);
  public final static native long new_UltCreditCardSdkParallelDeliveryCallback();
  public final static native void delete_UltCreditCardSdkParallelDeliveryCallback(long jarg1);
  public final static native void UltCreditCardSdkParallelDeliveryCallback_onNewResult(long jarg1, UltCreditCardSdkParallelDeliveryCallback jarg1_, long jarg2, UltCreditCardSdkResult jarg2_);
  public final static native void UltCreditCardSdkParallelDeliveryCallback_director_connect(UltCreditCardSdkParallelDeliveryCallback obj, long cptr, boolean mem_own, boolean weak_global);
  public final static native void UltCreditCardSdkParallelDeliveryCallback_change_ownership(UltCreditCardSdkParallelDeliveryCallback obj, long cptr, boolean take_or_release);
  public final static native long UltCreditCardSdkEngine_init__SWIG_0(String jarg1);
  public final static native long UltCreditCardSdkEngine_init__SWIG_1();
  public final static native long UltCreditCardSdkEngine_deInit();
  public final static native long UltCreditCardSdkEngine_process__SWIG_0(int jarg1, java.nio.ByteBuffer jarg2, long jarg3, long jarg4, long jarg5, int jarg6);
  public final static native long UltCreditCardSdkEngine_process__SWIG_1(int jarg1, java.nio.ByteBuffer jarg2, long jarg3, long jarg4, long jarg5);
  public final static native long UltCreditCardSdkEngine_process__SWIG_2(int jarg1, java.nio.ByteBuffer jarg2, long jarg3, long jarg4);
  public final static native long UltCreditCardSdkEngine_process__SWIG_3(int jarg1, java.nio.ByteBuffer jarg2, java.nio.ByteBuffer jarg3, java.nio.ByteBuffer jarg4, long jarg5, long jarg6, long jarg7, long jarg8, long jarg9, long jarg10, int jarg11);
  public final static native long UltCreditCardSdkEngine_process__SWIG_4(int jarg1, java.nio.ByteBuffer jarg2, java.nio.ByteBuffer jarg3, java.nio.ByteBuffer jarg4, long jarg5, long jarg6, long jarg7, long jarg8, long jarg9, long jarg10);
  public final static native long UltCreditCardSdkEngine_process__SWIG_5(int jarg1, java.nio.ByteBuffer jarg2, java.nio.ByteBuffer jarg3, java.nio.ByteBuffer jarg4, long jarg5, long jarg6, long jarg7, long jarg8, long jarg9);
  public final static native long UltCreditCardSdkEngine_requestRuntimeLicenseKey__SWIG_0(boolean jarg1);
  public final static native long UltCreditCardSdkEngine_requestRuntimeLicenseKey__SWIG_1();
  public final static native long UltCreditCardSdkEngine_warmUp(int jarg1);
  public final static native void delete_UltCreditCardSdkEngine(long jarg1);

  public static void SwigDirector_UltCreditCardSdkParallelDeliveryCallback_onNewResult(UltCreditCardSdkParallelDeliveryCallback self, long result) {
    self.onNewResult((result == 0) ? null : new UltCreditCardSdkResult(result, false));
  }

  private final static native void swig_module_init();
  static {
    swig_module_init();
  }
}
