package creational_pattern.singleton_pattern;

/**
 * 同步锁单例模式
 */
public class Singleton2 {
    // 统一的静态变量
    private static Singleton2 singleton;

    /**
     * 构造方法私有化
     */
    private Singleton2(){}

    /**
     * 构建统一的获取对象的入口 synchronized保证其线程安全
     *
     * @return
     */
    private static synchronized Singleton2 getInstance(){
        // 条件判断加锁
        synchronized (Singleton2.class){
            if (null == singleton){
                singleton = new Singleton2();
                return singleton;
            }
        }
        return singleton;
    }


    private static synchronized Singleton2 getInstance2(){
        // 双重条件判断加锁
        synchronized (Singleton2.class){
            if (null == singleton){
                synchronized (Singleton2.class){
                    if(null == singleton){
                        singleton = new Singleton2();
                        return singleton;
                    }
                }
            }
        }
        return singleton;
    }
}
