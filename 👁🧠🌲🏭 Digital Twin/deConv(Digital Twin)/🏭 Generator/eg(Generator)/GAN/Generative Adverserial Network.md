
The main goal of this 2022 summer project (advised by Ali Hirsa and Garud Iyengar) is to understand the geology of GAN; how it became diversified and what properties of data generating process each GANs is targeting. If time permits, we target to suggest a new GAN (or other) learning network targeted for time series i.e. sequential model which includes finance.  
  
GAN is categorized as implicit density in the statistical learning methodology family. Getting the maximum likelihood (or with prior, posterior) is the basic setting for statistical inference. This diverges into explicit or implicit density. GANs are the example of implicit density and explicit density can further diverge into tractable (auto-regressive) or approximate density (VAE).  
  
The history of GANs can be described as five steps and for each, understanding its loss function, network architecture, and how learning is performed (using gradient descent for instance) are the key. The orders are 
1. vanilla GAN
2. Quant GAN (Temporal convolution network)
3. Reg GAN (which has additional pre-trained Discriminator2 and uses geometric properties. It uses stylized facts such as skewness, kurtosis, volatility clusters) 
4. Temporal attention GAN
5. Temporal transformer GAN

| -                     | loss function | training | minimax |
| --------------------- | ------------- | -------- | ------- |
| vallina GANs          |               |          |         |
| QuantGAN              |               |          |         |
| RegGAN                |               |          |         |
| Temporal attention    |               |          |         |
| Temporal  transformer |               |          |         |


### loss
1. D_loss = D_loss_real + D_loss_fake
- $\alpha$-error: D_loss_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(`D_logit_real`, tf.ones_like(D_logit_real))) 
- $\beta$-error: D_loss_fake = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(D_logit_fake, tf.zeros_like(`D_logit_real`)))

2. G_loss
= tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(D_logit_fake, tf.ones_like(D_logit_fake)))