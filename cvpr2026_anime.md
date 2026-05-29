# CVPR 2026 — Anime / Illustration Domain Papers

**Total: 54 papers** | Poster: 41 | Project page: 15 | 和訳済み: 54

*Generated: 2026-05-29 11:23*

> 📝 **データソース:** `anime_enriched.json` — レイアウト変更は `generate_md.py` を編集後に再実行してください。

---

## 1. Modeling the Visual Ambiguity of Human Sketches

> 🇯🇵 **人間スケッチの視覚的曖昧性のモデリング**

> 💡 人間スケッチの曖昧性をモデル化して認識。

**著者:** Yang Zhou, Ping Ni, Jin Wang, Senyun Jia, Jingdan Yan, Kaixiang Huang, Guodong Lu, Jingru Yang, Shengfeng He

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Modeling_the_Visual_Ambiguity_of_Human_Sketches_CVPR_2026_paper.html)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/39560.png)


**Abstract:** Human sketches provide a compact and expressive form of visual communication, but their sparse structural cues, while capturing essential object structures, introduce ambiguity because a single sketch can correspond to multiple plausible images, making cross-domain alignment uncertain and unstable. Such ambiguity fundamentally limits sketch-based vision tasks that rely on precise sketch--image correspondence. To address this challenge, we introduce AmbiScore, a metric that quantifies the ambiguity of sketch-image pairs, and use Zero-Shot Sketch-Based Image Retrieval (ZS-SBIR) as a testbed to reveal how ambiguous supervision leads to performance collapse in existing methods. We further propose DisAmb (Disentangling Ambiguity), a framework that explicitly models and mitigates ambiguity through two components: (1) Elastic Matching, which adaptively adjusts supervision strength using AmbiScore, and (2) Purified Matching, which employs ambiguity-agnostic masks to disentangle structure and appearance via shape jigsaw and texture swapping. DisAmb establishes new benchmarks under high ambiguity and provides a robust, transferable supervisory signal for downstream sketch-guided tasks.


---

## 2. Vector Prism: Animating Vector Graphics by Stratifying Semantic Structure

> 🇯🇵 **Vector Prism：セマンティック構造の層別化によるベクトルグラフィック動画化**

> 💡 SVGのセマンティック構造を層別化して動画化し効率化。

**著者:** Jooyeol Yun, Jaegul Choo

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yun_Vector_Prism_Animating_Vector_Graphics_by_Stratifying_Semantic_Structure_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.14336) | [🌐 Project](https://yeolj00.github.io/research/vector-prism/)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/38438.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://yeolj00.github.io/research/vector-prism/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Scalable Vector Graphics (SVG) are central to modern web design, and the demand to animate them continues to grow as web environments become increasingly dynamic.Yet automating the animation of vector graphics remains challenging for vision–language models (VLMs) despite recent progress in code generation and motion planning.VLMs routinely mis-handle SVGs, since visually coherent parts are often fragmented into low-level shapes that offer little guidance of which elements should move together. In this paper, we introduce a framework that recovers the semantic structure required for reliable SVG animation and reveals the missing layer that current VLM systems overlook. This is achieved through a statistical aggregation of multiple weak part predictions, allowing the system to stably infer semantics from noisy predictions.By reorganizing SVGs into semantic groups, our approach enables VLMs to produce animations with far greater coherence. Our experiments demonstrate substantial gains over existing approaches, suggesting that semantic recovery is the key step that unlocks robust SVG animation and supports more interpretable interactions between VLMs and vector graphics.


---

## 3. Animator-Centric Skeleton Generation on Objects with Fine-Grained Details

> 🇯🇵 **精細な詳細を持つオブジェクトの動画中心スケルトン生成**

> 💡 動画中心設計で精細な詳細を持つスケルトン自動生成。

**著者:** Mingze Sun, Cheng Zeng, Pei Jiansong, Junhao Chen, Chaoyue Song, Shaohui Wang, Tianyuan Chang, Bin Huang, Zijiao Zeng, Ruqi Huang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Animator-Centric_Skeleton_Generation_on_Objects_with_Fine-Grained_Details_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2604.20539)

**Session:** Poster Session 3 & Exhibit Hall


> 🚫 Poster image not yet available


**Abstract:** Skeleton generation is essential for animating 3D assets, but current deep learning methods remain limited: they cannot handle the growing structural complexity of modern models and offer minimal controllability, creating a major bottleneck for real-world animation workflows. To address this, we propose an animator-centric SG framework that achieves high-quality skeleton prediction on complex inputs while providing intuitive control handles. Our contributions are threefold. First, we curate a large-scale dataset of 82,633 rigged meshes with diverse and complicated structures. Second, we introduce a novel semantic-aware tokenization scheme for auto-regressive modeling. This scheme effectively complements purely geometric prior methods by subdividing bones into semantically meaningful groups, thereby enhancing robustness to structural complexity and enabling a key control mechanism. Third, we design a learnable density interval module that allows animators to exert soft, direct control over bone density. Extensive experiments demonstrate that our framework not only generates high-quality skeletons for challenging inputs but also successfully fulfills two critical requirements from professional animators. Our work paves the way for more flexible and efficient animation pipelines.


---

## 4. Bridging Facial Understanding and Animation via Language Models

> 🇯🇵 **言語モデルを用いた顔理解とアニメーション接続**

> 💡 言語モデルで顔理解からアニメーションへシームレス接続。

**著者:** Luchuan Song, Pinxin Liu, Haiyang Liu, Zhenchao Jin, Yolo Yunlong Tang, Zichong Xu, Susan Liang, Jing Bi, Jason J. Corso, Chenliang Xu

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Song_Bridging_Facial_Understanding_and_Animation_via_Language_Models_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.16936) | [🌐 Project](https://songluchuan.github.io/TDMM-LM/)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/37694.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://songluchuan.github.io/TDMM-LM/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Text-guided human body animation has advanced rapidly, yet facial animation lags due to the scarcity of well-annotated, text-paired facial corpora. To close this gap, we leverage foundation generative models to synthesize a large, balanced corpus of facial behavior. We design prompts suite covering emotions and head motions, generate about 80 hours of facial videos with multiple generators, and fit per-frame 3D facial parameters, yielding large-scale (prompt and parameter) pairs for training. Building on this dataset, we probe language models for bidirectional competence over facial motion via two complementary tasks: (1) Motion2Language: given a sequence of 3D facial parameters, the model produces natural-language descriptions capturing content, style, and dynamics; and (2) Language2Motion: given a prompt, the model synthesizes the corresponding sequence of 3D facial parameters via quantized motion tokens for downstream animation. Extensive experiments show that in this setting language models can both interpret and synthesize facial motion with strong generalization. To best of our knowledge, this is the first work to cast facial-parameter modeling as a language problem, establishing a unified path for text-conditioned facial animation and motion understanding.


---

## 5. PersonaLive! Expressive Portrait Image Animation for Live Streaming

> 🇯🇵 **PersonaLive！ライブストリーミング用表現力豊かな肖像画像動画化**

> 💡 ライブストリーミング向け肖像画像の表現力豊か動画化。

**著者:** Zhiyuan Li, Chi-Man Pun, Chen Fang, Jue Wang, Xiaodong Cun

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_PersonaLive_Expressive_Portrait_Image_Animation_for_Live_Streaming_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.11253)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/37836.png)


**Abstract:** Current diffusion-based portrait animation models predominantly focus on enhancing visual quality and expression realism, while overlooking generation latency and real-time performance, which restricts their application range in the live streaming scenario. We propose PersonaLive, a novel diffusion-based framework towards streaming real-time portrait animation with multi-stage training recipes. Specifically, we first adopt hybrid implicit signals, namely implicit facial representations and 3D implicit keypoints, to achieve expressive image-level motion control. Then, a fewer-step appearance distillation strategy is proposed to eliminate appearance redundancy in the denoising process, greatly improving inference efficiency. Finally, we introduce an autoregressive micro-chunk streaming generation paradigm equipped with a sliding training strategy and a historical keyframe mechanism to enable low-latency and stable long-term video generation. Extensive experiments demonstrate that PersonaLive achieves state-of-the-art performance with up to **7-22**$\times$ speedup over prior diffusion-based portrait animation models. The code will be publicly available.


---

## 6. Zero-Shot Reconstruction of Animatable 3D Avatars with Cloth Dynamics from a Single Image

> 🇯🇵 **単一画像からのクロスダイナミクス付き動画可能3Dアバターのゼロショット再構成**

> 💡 単一画像からクロス動画と衣服物理で3Dアバター再構成。

**著者:** Joohyun Kwon, Geonhee Sim, Gyeongsik Moon

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Kwon_Zero-Shot_Reconstruction_of_Animatable_3D_Avatars_with_Cloth_Dynamics_from_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.14772)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/40009.png)


**Abstract:** Existing single-image 3D human avatar methods primarily rely on rigid joint transformations, limiting their ability to model realistic cloth dynamics. We present DynaAvatar, a zero-shot framework that reconstructs animatable 3D human avatars with motion-dependent cloth dynamics from a single image. Trained on large-scale multi-person motion datasets, DynaAvatar employs a Transformer-based feed-forward architecture that directly predicts dynamic 3D Gaussian deformations without subject-specific optimization. To overcome the scarcity of dynamic captures, we introduce a static-to-dynamic knowledge transfer strategy: a Transformer pretrained on large-scale static captures provides strong geometric and appearance priors, which are efficiently adapted to motion-dependent deformations through lightweight LoRA fine-tuning on dynamic captures. We further propose the DynaFlow loss, an optical flow–guided objective that provides reliable motion-direction geometric cues for cloth dynamics in rendered space. Finally, we reannotate the missing or noisy SMPL-X fittings in existing dynamic capture datasets, as most public dynamic capture datasets contain incomplete or unreliable fittings that are unsuitable for training high-quality 3D avatar reconstruction models. Experiments demonstrate that DynaAvatar produces visually rich and generalizable animations, outperforming prior methods. Code, pretrained models, and reannotations will be released.


---

## 7. FlexAvatar: Flexible Large Reconstruction Model for Animatable Gaussian Head Avatars with Detailed Deformation

> 🇯🇵 **FlexAvatar：詳細変形付き動画可能ガウシアンヘッドアバターの柔軟大規模再構成**

> 💡 詳細変形対応ガウシアンヘッドアバターの柔軟再構成。

**著者:** Cheng Peng, Zhuo Su, Liao Wang, Chen Guo, Zhaohu Li, Chengjiang Long, Zheng Lv, Jingxiang Sun, Chenyangguang Zhang, Yebin Liu

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Peng_FlexAvatar_Flexible_Large_Reconstruction_Model_for_Animatable_Gaussian_Head_Avatars_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.17717) | [🌐 Project](https://pengc02.github.io/flexavatar/)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/36626.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://pengc02.github.io/flexavatar/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** We present FlexAvatar, a flexible large reconstruction model for high-fidelity 3D head avatars with detailed dynamic deformation from single or sparse images, without requiring camera poses or expression labels. It leverages a transformer-based reconstruction model with structured head query tokens as canonical anchor to aggregate flexible input-number-agnostic, camera-pose-free and expression-free inputs into a robust canonical 3D representation.For detailed dynamic deformation, we introduce a lightweight UNet decoder conditioned on UV-space position maps, which can produce detailed expression-dependent deformations in real time. To better capture rare but critical expressions like wrinkles and bared teeth, we also adopt a data distribution adjustment strategy during training to balance the distribution of these expressions in the training set.Moreover, a lightweight 10-second refinement can further enhances identity-specific details in extreme identities without affecting deformation quality.Extensive experiments demonstrate that our FlexAvatar achieves superior 3D consistency, detailed dynamic realism compared with previous methods, providing a practical solution for animatable 3D avatar creation.


---

## 8. From Sketch to Fresco: Efficient Diffusion Transformer with Progressive Resolution

> 🇯🇵 **スケッチからフレスコまで：段階的解像度を持つ効率的拡散トランスフォーマー**

> 💡 段階的解像度拡散で効率的にスケッチからアート生成。

**著者:** Shikang Zheng, Guantao Chen, Landis He, Jiacheng Liu, Yuqi Lin, Chang Zou, Linfeng Zhang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zheng_From_Sketch_to_Fresco_Efficient_Diffusion_Transformer_with_Progressive_Resolution_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2601.07462)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/36967.png)


**Abstract:** Diffusion Transformers achieve impressive generative quality but remain computationally expensive due to iterative sampling.  Recently, dynamic resolution sampling has emerged as a promising acceleration technique by reducing the resolution of early sampling steps. However, existing methods rely on heuristic re-noising at every resolution transition, injecting noise that breaks cross-stage consistency and forces the model to relearn global structure. In addition, these methods indiscriminately upsample the entire latent space at once without checking which regions have actually converged, causing accumulated errors, and visible artifacts. Therefore, we propose \textbf{Fresco}, a dynamic resolution framework that unifies re-noise and global structure across stages with progressive upsampling, preserving both the efficiency of low-resolution drafting and the fidelity of high-resolution refinement, with all stages aligned toward the same final target. Fresco achieves near-lossless acceleration across diverse domains and models, including 10$\times$ speedup on FLUX, and 5$\times$ on HunyuanVideo, while remaining orthogonal to distillation, quantization and feature caching, reaching 22$\times$ speedup when combined with distilled models. Our code is in supplementary material and will be released on Github.


---

## 9. Image-Guided Geometric Stylization of 3D Meshes

> 🇯🇵 **3Dメッシュの画像ガイド幾何学的スタイル化**

> 💡 画像ガイドで3Dメッシュを幾何学的スタイル化。

**著者:** Changwoon Choi, Hyunsoo Lee, Clément Jambon, Yael Vinker, Young Min Kim

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Choi_Image-Guided_Geometric_Stylization_of_3D_Meshes_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2604.07795) | [🌐 Project](https://changwoonchoi.github.io/GeoStyle/)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/38063.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://changwoonchoi.github.io/GeoStyle/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Recent generative models can create visually plausible 3D representations of objects. However, the generation process often allows for implicit control signals, such as contextual descriptions, and rarely supports bold geometric distortions beyond existing data distributions. We propose a geometric stylization framework that deforms a 3D mesh, allowing it to express the style of an image. While style is inherently ambiguous, we utilize pre-trained diffusion models to extract an abstract representation of the provided image. Our coarse-to-fine stylization pipeline can drastically deform the input 3D model to express a diverse range of geometric variations while retaining the valid topology of the original mesh and part-level semantics. We also propose an approximate VAE encoder that provides efficient and reliable gradients from mesh renderings. Extensive experiments demonstrate that our method can create stylized 3D meshes that reflect unique geometric features of the pictured assets, such as expressive poses and silhouettes, thereby supporting the creation of distinctive artistic 3D creations.


---

## 10. Action-Sketcher: From Reasoning to Action via Visual Sketches for Robotic Manipulation

> 🇯🇵 **Action-Sketcher：ロボット操作のための視覚スケッチを通じた推論から行動へ**

> 💡 視覚スケッチで推論からロボット行動へ変換。

**著者:** Huajie Tan, Peterson Co, Yijie Xu, Shanyu Rong, Yuheng Ji, Cheng Chi, Xiansheng Chen, Zhongxia Zhao, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Tan_Action-Sketcher_From_Reasoning_to_Action_via_Visual_Sketches_for_Robotic_CVPR_2026_paper.html)

**Session:** Poster Session 4 & Exhibit Hall w/ Coffee Break


> 🚫 Poster image not yet available


**Abstract:** Long-horizon, open-world robotic manipulation is increasingly important for real-world deployment, requiring spatial disambiguation in complex layouts and temporal resilience under dynamic interaction. However, existing end-to-end and hierarchical Vision–Language–Action (VLA) policies often rely on text-only cues while keeping plan intent latent, which undermines \textit{referential grounding} in cluttered or underspecified scenes, impedes effective \textit{task decomposition} of long-horizon goals with close-loop interaction, and limits \textit{causal explanation} by obscuring the rationale behind action choices. To address these issues, we first introduce \textbf{Visual Sketch}, a lightweight visual intermediate that renders points, boxes, arrows, and typed relations on the robot’s current views to externalize spatial intent, bind language to scene geometry, and provide a human-verifiable bridge between high-level reasoning and low-level control. Building on \textit{Visual Sketch}, we present \textbf{Action-Sketcher}, a VLA framework that operates in a cyclic \textit{See $\rightarrow$ Think $\rightarrow$ Sketch $\rightarrow$ Act} workflow coordinated by adaptive token-gated strategy for reasoning triggers, sketch revision, and action issuance, thereby supporting reactive corrections and human interaction while preserving real-time action prediction. To enable scalable training and evaluation, we curate a 2.3M-sample corpus with interleaved images, text, \textit{Visual Sketch} supervision, and action sequences, and train \textit{Action-Sketcher} with a multi-stage curriculum recipe that combines interleaved sequence alignment for modality unification, language-to-sketch consistency for precise linguistic grounding, and imitation learning augmented with sketch-to-action reinforcement for robustness. Experiments on cluttered tabletops and multi-object tasks, in simulation and on real robots, show improved long-horizon success, stronger robustness to dynamic scene changes, and enhanced interpretability via editable sketches and step-wise plans.


---

## 11. PC-Talk: Precise Facial Animation Control for Audio-Driven Talking Face Generation

> 🇯🇵 **PC-Talk：音声駆動トーキングフェース生成の精密顔アニメーション制御**

> 💡 音声駆動で精密な顔アニメーション制御を実現。

**著者:** baiqin wang, Xiangyu Zhu, Fan Shen, HAO XU, Zhen Lei

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_PC-Talk_Precise_Facial_Animation_Control_for_Audio-Driven_Talking_Face_Generation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2503.14295)

**Session:** Poster Session 4 & Exhibit Hall w/ Coffee Break


![Poster](posters/anime/39419.png)


**Abstract:** Recent advancements in audio-driven talking face generation have made great progress in lip synchronization. However, current methods often lack sufficient control over talking face, such as speaking style and emotional expression, resulting in uniform facial motion. In this paper, we focus on improving two key factors: lip-audio alignment control(LAC) and emotion control(EMC), to enhance the diversity and user-friendliness of talking videos. Lip-audio alignment control ensures accurate lip-sync across varied speaking styles to simulate different talking habits, whereas emotion control aims to generate realistic emotional expressions with varying intensities and mixed emotional states. To achieve precise facial animation control, we propose a novel and efficient framework, PC-Talk, which enables lip-audio alignment control and emotion control through implicit keypoint deformations. First, our LAC module generates lip-synced talking faces with a specific speaking style, derived from either a video reference or preset options. It also supports lip movement scale adjustment and fine-grained editing of speaking styles for specific articulations. Second, our EMC module produces vivid emotional facial expressions through pure emotional deformation. It further enables precise control over emotion intensity and the compound emotions across different facial regions. Our method demonstrates outstanding control capabilities and achieves state-of-the-art performance on HDTF and MEAD datasets in experiments. The code will be publicly available.


---

## 12. FlashPortrait: 6x Faster Infinite Portrait Animation with Adaptive Latent Prediction

> 🇯🇵 **FlashPortrait：適応潜在予測による無限肖像動画の6倍高速化**

> 💡 適応予測で肖像無限動画を6倍高速化。

**著者:** Shuyuan Tu, Yueming Pan, Yinming Huang, Xintong Han, Zhen Xing, Qi Dai, Kai Qiu, Chong Luo, Zuxuan Wu

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Tu_FlashPortrait_6x_Faster_Infinite_Portrait_Animation_with_Adaptive_Latent_Prediction_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.16900)

**Session:** Poster Session 4 & Exhibit Hall w/ Coffee Break


![Poster](posters/anime/38073.png)


**Abstract:** Current diffusion-based acceleration methods for long-portrait animation struggle to ensure identity (ID) consistency. This paper presents FlashPortrait, an end-to-end video diffusion transformer capable of synthesizing ID-preserving, infinite-length videos while achieving up to 6$\times$ acceleration in inference speed. In particular, FlashPortrait begins by computing the identity-agnostic facial expression features with an off-the-shelf extractor. It then introduces a Normalized Facial Expression Block to align facial features with diffusion latents by normalizing them with their respective means and variances, thereby improving identity stability in facial modeling. During inference, FlashPortrait adopts a dynamic sliding-window scheme with weighted blending in overlapping areas, ensuring smooth transitions and ID consistency in long animations. In each context window, based on the latent variation rate at particular timesteps and the derivative magnitude ratio among diffusion layers, FlashPortrait utilizes higher-order latent derivatives at the current timestep to directly predict latents at future timesteps, thereby skipping several denoising steps and achieving 6$\times$ speed acceleration. Experiments on benchmarks show the effectiveness of FlashPortrait both qualitatively and quantitatively.


---

## 13. HyperGaussians: High-Dimensional Gaussian Splatting for High-Fidelity Animatable Face Avatars

> 🇯🇵 **HyperGaussians：高忠実度動画可能顔アバターのための高次元ガウシアンスプラッティング**

> 💡 高次元ガウシアンスプラッティングで高忠実度顔アバター。

**著者:** Gent Serifi, Marcel C.

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Serifi_HyperGaussians_High-Dimensional_Gaussian_Splatting_for_High-Fidelity_Animatable_Face_Avatars_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2507.02803) | [🌐 Project](https://gserifi.github.io/HyperGaussians/)

**Session:** Poster Session 4 & Exhibit Hall w/ Coffee Break


![Poster](posters/anime/36405.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://gserifi.github.io/HyperGaussians/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** We introduce HyperGaussians, a novel extension of 3D Gaussian Splatting for high-quality animatable face avatars. While tremendous successes have been achieved for static faces, animatable avatars from dynamic videos still fall in the uncanny valley. The de facto standard, 3D Gaussian Splatting (3DGS), represents a face through a collection of 3D Gaussian primitives. 3DGS excels at rendering static faces, but the state-of-the-art still struggles with nonlinear deformations, complex lighting effects, and fine details. While most related works focus on predicting better Gaussian parameters from expression codes, we rethink the 3D Gaussian representation itself and how to make it more expressive. Our insights lead to a novel extension of 3D Gaussians to high-dimensional multivariate Gaussians, dubbed 'HyperGaussians'. The higher dimensionality increases expressivity through conditioning on a learnable local embedding. However, splatting HyperGaussians is computationally expensive because it requires inverting a high-dimensional covariance matrix. We solve this by reparameterizing the covariance matrix, dubbed the 'inverse covariance trick'. This trick boosts the efficiency so that HyperGaussians can be seamlessly integrated into existing models. To demonstrate this, we plug in HyperGaussians into two state-of-the-art methods for face avatars: FlashAvatar and GaussianHeadAvatar. Our evaluation on 29 subjects from 6 face datasets shows that HyperGaussians outperform 3DGS numerically and visually, particularly for high-frequency details like eyes, teeth, wrinkles, and specular reflections.


---

## 14. RigMo: Unifying Rig and Motion Learning for Generative Animation

> 🇯🇵 **RigMo：生成アニメーション用リグと動きの学習統一**

> 💡 リグと動き学習を統一した生成アニメーション。

**著者:** Hao Zhang, Jiahao Luo, Bohui Wan, Yizhou Zhao, Zongrui Li, Michael Vasilkovsky, Chaoyang Wang, Jian Wang, Narendra Ahuja, Bing Zhou

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_RigMo_Unifying_Rig_and_Motion_Learning_for_Generative_Animation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2601.06378)

**Session:** Poster Session 4 & Exhibit Hall w/ Coffee Break


> 🚫 Poster image not yet available


**Abstract:** Recent progress in 4D generation has advanced the reconstruction of dynamic geometry, yet the modeling of rig and motion, the two core elements of animation, remains disconnected. Existing approaches typically treat rigging and motion generation as independent tasks: auto-rigging methods rely on human-annotated skeletons and skinning weights, while motion-generation models predict dense vertex trajectories without any explicit structure. This separation contradicts the nature of animation itself, which is the coupled outcome of both structure and motion, and it limits scalability, interpretability, and control.We present RigMo, a unified generative framework that jointly learns rig and motion directly from raw mesh sequences without any rig annotations or human priors. RigMo encodes per-vertex deformations into a compact latent space and decodes a set of implicit Gaussian bones, skinning weights, and time-varying transformations that together define an animatable mesh. This design makes the model animatable by construction: a single latent representation yields both an explicit rig structure and temporally coherent motion parameters. Unlike optimization-based auto-rigging methods that overfit to a specific sequence, RigMo generalizes across object categories and motion styles, offering feed-forward inference for arbitrary deformable objects. Experiments on DeformingThings4D, Objaverse-XL, and diverse human and animal datasets demonstrate that RigMo generates smooth, interpretable, and physically consistent rigs, achieving superior reconstruction and generalization compared to existing 4D generative baselines. RigMo establishes a new paradigm for structure-aware, controllable, and scalable 4D generation.


---

## 15. Illustrator’s Depth: Monocular Layer Index Prediction for Image Decomposition

> 🇯🇵 **イラストレーターの深さ：モノキュラー層インデックス予測による画像分解**

> 💡 デジタルコンテンツ制作向けに、平坦画像を編集可能な順序付き層に分解するための層インデックス予測手法。

**著者:** Nissim Maruani, Peiying Zhang, Siddhartha Chaudhuri, Matthew Fisher, Nanxuan Zhao, Vladimir G. Kim, Pierre Alliez, Mathieu Desbrun, Wang Yifan

**Links:** [📄 Paper](https://cvpr.thecvf.com/virtual/2026/poster/38824)

**Session:** Poster Session 4 & Exhibit Hall w/ Coffee Break


> 🚫 Poster image not yet available


**Abstract:** We introduce Illustrator’s Depth, a novel definition of depth that addresses a key challenge in digital content creation: decomposing flat images into editable, ordered layers. Inspired by an artist’s compositional process, illustrator’s depth infers a layer index to each pixel, forming an interpretable image decomposition through a discrete, globally consistent ordering of elements optimized for editability. We also propose and train a neural network using a curated dataset of layered vector graphics to predict layering directly from raster inputs. Our layer index inference unlocks a range of powerful downstream applications. In particular, it significantly outperforms state-of-the-art baselines for image vectorization while also enabling high-fidelity text-to-vector-graphics generation, automatic 3D relief generation from 2D images, and intuitive depth-aware editing. By reframing depth from a physical quantity to a creative abstraction, illustrator's depth prediction offers a new foundation for editable image decomposition.


---

## 16. Hist2Style: Histogram-Guided Stylization with Bilateral Grids

> 🇯🇵 **Hist2Style：ヒストグラム誘導スタイライゼーション（両側グリッド利用）**

> 💡 ヒストグラムベースのスタイル埋め込みを使用した高速でエッジ保存的なスタイル転送手法。

**著者:** Dekel Galor, Adam Pikielny, Zhoutong Zhang, Ke Wang, Laura Waller, Jiawen Chen, Ilya Chugunov

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Galor_Hist2Style_Histogram-Guided_Stylization_with_Bilateral_Grids_CVPR_2026_paper.html) | [🌐 Project](https://www.dekelgalor.com/hist2style)

**Session:** Poster Session 5 & Exhibit Hall


> 🚫 Poster image not yet available


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://www.dekelgalor.com/hist2style" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Photorealistic style transfer aims to match the color and tone of an input image to that of a style target while preserving the content and details of the original scene. Although existing large image models can facilitate these kinds of appearance edits, their high computational demands, potential for hallucinations, and limited user control make them unsuitable for high-resolution, real-time workflows. We introduce Hist2Style, a bilateral-grid formulation for fast, edge-aware stylization that preserves visual fidelity by constraining operations to locally affine transforms in bilateral space. Our model is trained to reproduce the spatially varying color edits available in larger image editing models. This training paradigm involves generating a large supervised corpus with language and vision-language models and distilling a high-capacity editor into a lightweight model. The model conditions on a histogram-based embedding of the style target, which provides an interpretable interface for adjusting the output style by modifying the target color distribution. Overall, Hist2Style maintains content structure by construction, avoids hallucinations, and supports real-time, high-resolution photorealistic stylization with interactive user-controllable color and tone adjustments.


---

## 17. Mixture of Style Experts for Diverse Image Stylization

> 🇯🇵 **スタイル専門家の混合：多様な画像スタイライゼーション**

> 💡 Mixture of Experts アーキテクチャを使用した意味認識スタイライゼーション手法。

**著者:** Shihao Zhu, Ziheng Ouyang, Yijia Kang, Qilong Wang, Mi Zhou, Bo Li, Mingming Cheng, Qibin Hou

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Mixture_of_Style_Experts_for_Diverse_Image_Stylization_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.16649)

**Session:** Poster Session 5 & Exhibit Hall


> 🚫 Poster image not yet available


**Abstract:** Diffusion-based stylization has advanced significantly, yet existing methods are limited to color-driven transformations, neglecting complex semantics and material details. We introduce StyleExpert, a semantic-aware framework based on Mixture of Experts (MoE).Our framework employs a unified style encoder, trained on our large-scale dataset of content-style-stylized triplets, to embed diverse styles into a consistent latent space. This embedding is then used to condition a similarity-aware gating mechanism, which dynamically routes styles to specialized experts within the MoE architecture. Leveraging this MoE architecture, our method adeptly handles diverse styles spanning multiple semantic levels, from shallow textures to deep semantics. Extensive experiments show that StyleExpert outperforms existing approaches in preserving semantics and material details, while generalizing to unseen styles.


---

## 18. PoseMaster: A Unified 3D Native Framework for Stylized Pose Generation

> 🇯🇵 **PoseMaster：3D ネイティブスタイル付きポーズ生成統合フレームワーク**

> 💡 3D スケルトンを直接利用した、ポーズスタイル化と3D生成を統合するフレームワーク。

**著者:** Hongyu Yan, Kunming Luo, Weiyu Li, Kaiyi Zhang, Yixun Liang, Jingwei Huang, Chunchao Guo, Ping Tan

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yan_PoseMaster_A_Unified_3D_Native_Framework_for_Stylized_Pose_Generation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2506.21076)

**Session:** Poster Session 5 & Exhibit Hall


![Poster](posters/anime/37775.png)


**Abstract:** Pose stylization is a fundamental task across the 2D, 3D, or video fields, which aim to output a stylized image or 3D mesh with the expected pose. In the 3D domains, existing pose stylization methods typically rely on 2D foundational models to modify the pose of an image before generating the corresponding 3D assets, which limits the ability of these methods to achieve rich and precise 3D pose stylization. To address this challenge, we propose a novel paradigm for 3D pose stylization that unifies pose stylization and 3D generation within a cohesive framework. This integration minimizes the risk of cumulative errors and enhances the model's efficiency and effectiveness. In addition, instead of a 2D skeleton used in previous works, we directly utilize the 3D skeleton because it can provide a more accurate representation of 3D spatial and topological relationships, which significantly enhances the model's capacity to achieve richer and more precise pose stylization. Additionally, we establish a comprehensive data engine to create a large-scale dataset that includes pairs of image-body misalignment and skeleton-body alignment. This dataset encourages 3D generative models to concurrently learn both the style of images and the pose-related 3D structures. Building on these innovations, we present PoseMaster, a unified 3D native method for stylized pose generation. Extensive experimental evaluations demonstrate that PoseMaster significantly outperforms current state-of-the-art techniques in both qualitative and quantitative assessments.


---

## 19. LottieGPT: Tokenizing Vector Animation for Autoregressive Generation

> 🇯🇵 **LottieGPT：ベクターアニメーション自動回帰生成のためのトークン化**

> 💡 Lottie JSON 形式のベクターアニメーション自動生成フレームワーク。

**著者:** Junhao Chen, Gao Kejun, Yuehan Cui, Mingze Sun, Mingjin Chen, Shaohui Wang, Xiaoxiao Long, Fei Ma, Qi Tian, Hao Zhao, Ruqi Huang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_LottieGPT_Tokenizing_Vector_Animation_for_Autoregressive_Generation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2604.11792)

**Session:** Poster Session 5 & Exhibit Hall


![Poster](posters/anime/38557.png)


**Abstract:** Despite rapid progress in video generation, existing models are incapable of producing vector animation, a dominant and highly expressive form of multimedia on the Internet. Vector animations offer resolution-independence, compactness, semantic structure, and editable parametric motion representations, yet current generative models operate exclusively in raster space and thus cannot synthesize them. Meanwhile, recent advances in large multimodal models demonstrate strong capabilities in generating structured data such as slides , 3D meshes , LEGO sequences , and indoor layouts , suggesting that native vector animation generation may be achievable. In this work, we present the first framework for tokenizing and autoregressively generating vector animations. We adopt Lottie, a widely deployed JSON-based animation standard, and design a tailored Lottie Tokenizer that encodes layered geometric primitives, transforms, and keyframe-based motion into a compact and semantically aligned token sequence. To support large-scale training, we also construct \textbf{LottieAnimation-660K}, the largest and most diverse vector animation dataset to date, consisting of 660k real-world Lottie animation and 15M static Lottie image files curated from broad Internet sources. Building upon these components, we finetune Qwen-VL to create \textbf{LottieGPT}, a native multimodal model capable of generating coherent, editable vector animations directly from natural language or visual prompts. Experiments show that our tokenizer dramatically reduces sequence length while preserving structural fidelity, enabling effective autoregressive learning of dynamic vector content. LottieGPT exhibits strong generalization across diverse animation styles and outperforms previous state-of-the-art models on SVG generation (a special case of single-frame vector animation).


---

## 20. PhysSkin: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning

> 🇯🇵 **PhysSkin：自己教師あり神経スキニングによるリアルタイム物理ベースアニメーション**

> 💡 リニアブレンドスキニングの概念を拡張した、メッシュフリーで汎用的な物理ベースアニメーション。

**著者:** Yuanhang Lei, Tao Cheng, Xingxuan Li, Boming Zhao, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Lei_PhysSkin_Real-Time_and_Generalizable_Physics-Based_Animation_via_Self-Supervised_Neural_Skinning_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.23194)

**Session:** Poster Session 5 & Exhibit Hall


![Poster](posters/anime/39227.png)


**Abstract:** Achieving real-time physics-based animation that generalizes across diverse 3D shapes and discretizations remains a fundamental challenge. We introduce PhysSkin, a physics-informed framework that addresses this challenge. In the spirit of Linear Blend Skinning, we learn continuous skinning fields as basis functions lifting motion subspace coordinates to full-space deformation, with subspace defined by handle transformations. To generate mesh-free, discretization-agnostic, and physically consistent skinning fields that generalize well across diverse 3D shapes, PhysSkin employs a new neural skinning fields autoencoder which consists of a transformer-based encoder and a cross-attention decoder.Furthermore, we also develop a novel physics-informed self-supervised learning strategy that incorporates on-the-fly skinning-field normalization and conflict-aware gradient correction, enabling effective balancing of energy minimization, spatial smoothness, and orthogonality constraints.PhysSkin shows outstanding performance on generalizable neural skinning and enables real-time physics-based animation.


---

## 21. FG-Portrait: 3D Flow Guided Editable Portrait Animation

> 🇯🇵 **FG-Portrait：3D フロー誘導編集可能ポートレートアニメーション**

> 💡 パラメトリック3D頭部モデルから計算した3Dフローを利用したポートレートアニメーション。

**著者:** Yating Xu, Yunqi Miao, Evangelos Ververas, Jiankang Deng, Jifei Song

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xu_FG-Portrait_3D_Flow_Guided_Editable_Portrait_Animation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.23381)

**Session:** Poster Session 5 & Exhibit Hall


![Poster](posters/anime/37400.png)


**Abstract:** Motion transfer from the driving to the source portrait remains a key challenge in the portrait animation. Current diffusion-based approaches condition only on the driving motion, which fails to capture source-to-driving correspondences and consequently yields suboptimal motion transfer.  Although flow estimation provides an alternative, predicting dense correspondences from 2D input is ill-posed and often yields inaccurate animation. We address this problem by introducing 3D flows, a learning-free and geometry-driven motion correspondence directly computed from parametric 3D head models. To integrate this 3D prior into diffusion model, we introduce 3D flow encoding to query potential 3D flows for each target pixel to indicate its displacement back to the source location. To obtain 3D flows aligned with 2D motion changes, we further propose depth-guided sampling to accurately locate the corresponding 3D points for each pixel. Beyond high-fidelity portrait animation, our model further supports user-specified editing of facial expression and head pose. Extensive experiments demonstrate the superiority of our method on consistent driving motion transfer as well as faithful source identity preservation. The source code will be released upon acceptance.


---

## 22. Order Matters: 3D Shape Generation from Sequential VR Sketches

> 🇯🇵 **Order Matters：連続 VR スケッチからの3D シェイプ生成**

> 💡 VR スケッチの時間的順序を考慮した、最初の3D シェイプ生成フレームワーク。

**著者:** Yizi Chen, Sidi Wu, Tianyi Xiao, Nina Wiedemann, Loic Landrieu

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_Order_Matters_3D_Shape_Generation_from_Sequential_VR_Sketches_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.04761)

**Session:** Poster Session 5 & Exhibit Hall


> 🚫 Poster image not yet available


**Abstract:** VR sketching lets users explore and iterate on ideas directly in 3D, offering a faster and more intuitive alternative to conventional CAD software. However, existing sketch-to-shape models ignore the temporal ordering of strokes, discarding crucial cues about structure and design intent. We introduce VRSketch2Shape, the first framework and multi-category dataset for 3D shape generation from sequential VR sketches. Our contributions are threefold: (i) an automated pipeline that generates ordered VR sketches from arbitrary shapes, (ii) a dataset comprising over 20k synthetic and 900 hand-drawn sketch–shape pairs across four categories, and (iii) an order-aware sketch encoder coupled with a diffusion-based 3D generator. Our approach yields higher geometric fidelity than prior work and generalizes effectively from synthetic to real sketches with minimal supervision. All data and models will be released in open access.


---

## 23. DreamStyle: A Unified Framework for Video Stylization

> 🇯🇵 **DreamStyle：ビデオスタイライゼーション統合フレームワーク**

> 💡 テキスト、スタイル画像、フレームの3つのスタイル条件に対応したビデオスタイライゼーション。

**著者:** Mengtian Li, Jinshu Chen, Songtao Zhao, Wanquan Feng, Pengqi Tu, Qian HE

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_DreamStyle_A_Unified_Framework_for_Video_Stylization_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2601.02785) | [🌐 Project](https://lemonsky1995.github.io/dreamstyle)

**Session:** Poster Session 5 & Exhibit Hall


![Poster](posters/anime/40188.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://lemonsky1995.github.io/dreamstyle" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Video stylization, an important downstream task of video generation models, has not yet been thoroughly explored. Its input style conditions typically include text, style image, and stylized first frame. Each condition has a characteristic advantage: text is more flexible, style image provides a more accurate visual anchor, and stylized first frame makes long-video stylization feasible. However, existing methods are largely confined to a single type of style condition, which limits their scope of application. Additionally, their lack of high-quality datasets leads to style inconsistency and temporal flicker. To address these limitations, we introduce DreamStyle, a unified framework for video stylization, supporting (1) text-guided, (2) style-image-guided, and (3) first-frame-guided video stylization, accompanied by a well-designed data curation pipeline to acquire high-quality paired video data. DreamStyle is built on a vanilla Image-to-Video (I2V) model and trained using a Low-Rank Adaptation (LoRA) with token-specific up matrices that reduces the confusion among different condition tokens. Both qualitative and quantitative evaluations demonstrate that DreamStyle is competent in all three video stylization tasks, and outperforms the competitors in style consistency and video quality.


---

## 24. Sketch2CT: Multimodal Diffusion for Structure-Aware 3D Medical Volume Generation

> 🇯🇵 **Sketch2CT：マルチモーダル拡散による構造認識3D医療ボリューム生成**

> 💡 2D スケッチとテキスト記述を条件とした構造保存的な医療ボリューム生成。

**著者:** Delin An, Chaoli Wang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/An_Sketch2CT_Multimodal_Diffusion_for_Structure-Aware_3D_Medical_Volume_Generation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.22509)

**Session:** Poster Session 6


![Poster](posters/anime/36477.png)


**Abstract:** Diffusion probabilistic models have demonstrated significant potential in generating high-quality, realistic medical images, providing a promising solution to the persistent challenge of data scarcity in the medical field. Nevertheless, producing 3D medical volumes with anatomically consistent structures under multimodal conditions remains a complex and unresolved problem. We introduce Sketch2CT, a multimodal diffusion framework for structure-aware 3D medical volume generation, jointly guided by a user-provided 2D sketch and a textual description that captures 3D geometric semantics. The framework initially generates 3D segmentation masks of the target organ from random noise, conditioned on both modalities. To effectively align and fuse these inputs, we propose two key modules that refine sketch features with localized textual cues and integrate global sketch-text representations. Built upon a capsule-attention backbone, these modules leverage the complementary strengths of sketches and text to produce anatomically accurate organ shapes. The synthesized segmentation masks subsequently guide a latent diffusion model for 3D CT volume synthesis, enabling realistic reconstruction of organ appearances that are consistent with user-defined sketches and descriptions. Extensive experiments on public CT datasets demonstrate that Sketch2CT achieves superior performance in generating multimodal medical volumes. Its controllable, low-cost generation pipeline enables principled, efficient augmentation of medical datasets.


---

## 25. Human Geometry Distribution for 3D Animation Generation

> 🇯🇵 **人間幾何分布：3D アニメーション生成**

> 💡 衣服ダイナミクスのきめ細かい幾何学的詳細をモデル化した3D人間アニメーション生成。

**著者:** Xiangjun Tang, Biao Zhang, Peter Wonka

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Tang_Human_Geometry_Distribution_for_3D_Animation_Generation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.07459)

**Session:** Poster Session 6


![Poster](posters/anime/38222.png)


**Abstract:** Generating realistic human geometry animations remains a challenging task, as it requires modeling natural clothing dynamics with fine-grained geometric details under limited data. To address these challenges, we propose two novel designs. First, we propose a compact distribution-based latent representation that enables efficient and high-quality geometry generation. We improve upon previous work by establishing a more uniform mapping between SMPL and avatar geometries. Second, we introduce a generative animation model that fully exploits the diversity of limited motion data. We focus on short-term transitions while maintaining long-term consistency through an identity-conditioned design. These two designs formulate our method as a two-stage framework: the first stage learns a latent space, while the second learns to generate animations within this latent space. We conducted experiments on both our latent space and animation model. We demonstrate that our latent space produces high-fidelity human geometry surpassing previous methods (90% lower Chamfer Dist.). The animation model synthesizes diverse animations with detailed and natural dynamics (2.2 x higher user study score), achieving the best results across all evaluation metrics.


---

## 26. Towards Storytelling Animations: Joint Synthesis of Human and Camera Motions

> 🇯🇵 **物語アニメーションに向けて：人間とカメラモーション連合合成**

> 💡 キャラクターインタラクションとカメラ配置を統合生成する無条件拡散モデル。

**著者:** Boyuan Cheng, Yingjie Xi, Rui He, Jinhe Na, Ying Cao, Pengjie Wang, Jian Jun Zhang, Xiaosong Yang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Cheng_Towards_Storytelling_Animations_Joint_Synthesis_of_Human_and_Camera_Motions_CVPR_2026_paper.html)

**Session:** Poster Session 6


![Poster](posters/anime/36922.png)


**Abstract:** Animation relies heavily on effective cinematography to enhance narrative clarity and emotional resonance, yet crafting optimal character interactions and camera positioning remains a resource-intensive challenge. Existing methods typically require extensive, predefined datasets, which restrict their effectiveness when encountering unfamiliar character interactions or novel animation contexts. We introduce an innovative approach to jointly generate character interactions and camera placements through unconditional diffusion-based generative models. Our method leverages a unified framework to simultaneously synthesize realistic two-person motions and corresponding cinematographic compositions without relying on predefined visual datasets. By integrating 3D motion representations and Toric features, our diffusion model effectively captures spatial orientation and relative positioning, enabling coherent and expressive scene generation. Experiments demonstrate that our approach can autonomously produce diverse and plausible dual-character interactions coupled with compelling camera movements, enhancing creative flexibility in animated storytelling.


---

## 27. OmniLottie: Generating Vector Animations via Parameterized Lottie Tokens

> 🇯🇵 **OmniLottie：パラメータ化 Lottie トークンによるベクターアニメーション生成**

> 💡 マルチモーダル条件でパラメータ化されたベクターアニメーション生成フレームワーク。

**著者:** Yiying Yang, Wei Cheng, Sijin Chen, Honghao Fu, Xianfang Zeng, Yujun Cai, Gang Yu, Xingjun Ma

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_OmniLottie_Generating_Vector_Animations_via_Parameterized_Lottie_Tokens_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.02138)

**Session:** Poster Session 6


![Poster](posters/anime/37471.png)


**Abstract:** OmniLottie is a versatile framework that generates high-quality vector animations from multi-modal instructions, including interleaved texts, images, and videos. To fully parameterize vector animations for flexible motion and visual content control, we seek help from the Lottie representation, which encodes both shapes and animated behaviors in a single JSON file. Building upon a pretrained vision–language model (VLM), OmniLottie produces vivid, semantically aligned vector animations that adhere closely to multi-modal conditions. To avoid the complexity and irregularity of raw JSON structures, we introduce a dedicated Lottie tokenizer that transforms Lottie files into structured sequences of function calls representing shapes, animation commands, and their parameters.  This design enables the model to directly learn the underlying shape and animation priors from data, substantially improving generation stability and controllability. To further advance research in vector animation generation, we curate MMLottie-2M, a large-scale dataset of professionally designed vector animations paired with textual and visual annotations. Leveraging the well-designed tokenizer and our newly established dataset, OmniLottie demonstrates strong multi-modal conditional generation capabilities using a simple next-token prediction objective. For qualitative results, please refer to the generated animations rendered through standard Lottie players on the supplementary website.


---

## 28. DeX-Portrait: Disentangled and Expressive Portrait Animation via Explicit and Latent Motion Representations

> 🇯🇵 **DeX-Portrait：明示的・潜在的モーション表現によ分解表現的ポートレートアニメーション**

> 💡 頭部ポーズと表情を分離制御できるポートレートアニメーション手法。

**著者:** Yuxiang Shi, Zhe Li, Yanwen Wang, Hao Zhu, Xun Cao, Ligang Liu

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_DeX-Portrait_Disentangled_and_Expressive_Portrait_Animation_via_Explicit_and_Latent_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.15524) | [🌐 Project](https://syx132.github.io/DeX-Portrait/)

**Session:** Poster Session 6


![Poster](posters/anime/36826.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://syx132.github.io/DeX-Portrait/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Portrait animation from a single source image and a driving video is a long-standing problem.Recent approaches tend to adopt diffusion-based image/video generation models for realistic and expressive animation.However, none of these diffusion models realizes high-fidelity disentangled control between the head pose and facial expression, hindering applications like expression-only or pose-only editing and animation.To address this, we propose DeX-Portrait, a novel approach capable of generating expressive portrait animation driven by disentangled pose and expression signals.Specifically, we represent the pose as an explicit global transformation and the expression as an implicit latent code.First, we design a powerful motion trainer to learn both pose and expression encoders for extracting precise and decomposed driving signals.Then we propose to inject the pose transformation into the diffusion model through a dual-branch conditioning mechanism, and the expression latent through cross attention.Finally, we design a progressive hybrid classifier-free guidance for more faithful identity consistency.Experiments show that our method outperforms state-of-the-art baselines on both animation quality and disentangled controllability.


---

## 29. Motion-Aware Animatable Gaussian Avatars Deblurring

> 🇯🇵 **モーション認識アニメーション化ガウス分布アバター除振**

> 💡 モーション情報を活用したガウシアン スプラッティング アバターの除振処理。

**著者:** Muyao Niu, Yifan Zhan, Qingtian Zhu, Zhuoxiao Li, Wei Wang, Zhihang Zhong, Xiao Sun, Yinqiang Zheng

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Niu_Motion-Aware_Animatable_Gaussian_Avatars_Deblurring_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2411.16758) | [🌐 Project](https://github.com/MyNiuuu/MAD-Avatar)

**Session:** Poster Session 6


![Poster](posters/anime/37716.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://github.com/MyNiuuu/MAD-Avatar" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** The creation of 3D human avatars from multi-view videos is a significant yet challenging task in computer vision. However, existing techniques rely on high-quality, sharp images as input, which are often impractical to obtain in real-world scenarios due to variations in human motion speed and intensity. This paper introduces a novel method for directly reconstructing sharp 3D human Gaussian avatars from blurry videos. The proposed approach incorporates a 3D-aware, physics-based model of blur formation caused by human motion, together with a 3D human motion model designed to resolve ambiguities in motion-induced blur. This framework enables the joint optimization of the avatar representation and motion parameters from a coarse initialization. Comprehensive benchmarks are established using both a synthetic dataset and a real-world dataset captured with a 360-degree synchronous hybrid-exposure camera system. Extensive evaluations demonstrate the effectiveness and robustness of the model across diverse conditions.


---

## 30. AniMimic: Imitating 3D Animation from Video Priors

> 🇯🇵 **AniMimic：ビデオプライアーからの3Dアニメーション模倣**

> 💡 ビデオプライアーを使用した3D アニメーション生成モデル。

**著者:** Tianyi Xie, Yunuo Chen, Yaowei Guo, Yin Yang, Bolei Zhou, Demetri Terzopoulos, Ying Jiang, Chenfanfu Jiang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Xie_AniMimic_Imitating_3D_Animation_from_Video_Priors_CVPR_2026_paper.html)

**Session:** Poster Session 6


> 🚫 Poster image not yet available


**Abstract:** Creating realistic 3D animation remains a time-consuming and expertise-dependent process, requiring manual rigging, keyframing, and fine-tuning of complex motions. Meanwhile, video diffusion models have recently demonstrated remarkable motion imagination in 2D, generating dynamic and visually coherent motion from text or image prompts. However, their results lack explicit 3D structure and cannot be directly used for animation or simulation. We present AnimaMimic, a framework that animates static 3D meshes using motion priors learned from video diffusion models. Starting from an input mesh, AnimaMimic synthesizes a monocular animation video, automatically constructs a skeleton with skinning weights, and refines joint parameters through differentiable rendering and video-based supervision. To further enhance realism, we integrate a differentiable simulation module that refines mesh deformation through physically grounded soft-tissue dynamics. Our method bridges the creativity of video diffusion and the structural control of 3D rigged animation, producing physically plausible, temporally coherent, and artist-editable motion sequences that integrate seamlessly into standard animation pipelines.


---

## 31. Tracking-Guided 4D Generation: Foundation-Tracker Motion Priors for 3D Model Animation

> 🇯🇵 **追跡誘導4D生成：基盤トラッカーモーションプライアーによる3Dモデルアニメーション**

> 💡 追跡情報を誘導として使用した4D モデルアニメーション生成。

**著者:** Su Sun, Cheng Zhao, Himangi Mittal, Gaurav Mittal, Rohith Kukkala, Yingjie Chen, Mei Chen

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Tracking-Guided_4D_Generation_Foundation-Tracker_Motion_Priors_for_3D_Model_Animation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.06158)

**Session:** Poster Session 6


![Poster](posters/anime/36672.png)


**Abstract:** Generating dynamic 4D objects from sparse inputs is difficult because it demands joint preservation of appearance and motion coherence across views and time while suppressing artifacts and temporal drift. We hypothesize that the view discrepancy arises from supervision limited to pixel- or latent-space video-diffusion losses, which lack explicitly temporally aware, feature-level tracking guidance.We present \emph{Track4DGen}, a two-stage framework that couples a multi-view video diffusion model with a foundation point tracker and a hybrid 4D Gaussian Splatting (4D-GS) reconstructor. The central idea is to explicitly inject tracker-derived motion priors into intermediate feature representations for both multi-view video generation and 4D-GS. In Stage One, we enforce dense, feature-level point correspondences inside the diffusion generator, producing temporally consistent features that curb appearance drift and enhance cross-view coherence. In Stage Two, we reconstruct a dynamic 4D-GS using a hybrid motion encoding that concatenates co-located diffusion features (carrying Stage-One tracking priors) with Hex-plane features, and augment them with 4D Spherical Harmonics for higher-fidelity dynamics modeling.\emph{Track4DGen} surpasses baselines on both multi-view video generation and 4D generation benchmarks, yielding temporally stable, text-editable 4D assets. Lastly, we curate \emph{Sketchfab28}, a high-quality dataset for benchmarking object-centric 4D generation and fostering future research.


---

## 32. SketchRevive: Fine-Grained Pixel-to-Vector Sketch Completion with Diffusion-Prior-Guided Multimodal LLMs

> 🇯🇵 **SketchRevive：拡散プライアー誘導マルチモーダル LLM によるピクセル・ベクトルスケッチ完成**

> 💡 きめ細かいピクセル・ベクトル変換スケッチ完成手法。

**著者:** Ran Zuo, Haoxiang Hu, Chenxi Pei, Yanxuan Liu, Wenwen Qiang, Fang Liu, Xiaoming Deng, Cuixia Ma, Yong-Jin Liu

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zuo_SketchRevive_Fine-Grained_Pixel-to-Vector_Sketch_Completion_with_Diffusion-Prior-Guided_Multimodal_LLMs_CVPR_2026_paper.html)

**Session:** Poster Session 6


![Poster](posters/anime/37334.png)


**Abstract:** Transforming sparse, partial pixel sketches from diverse media into complete, editable vector drawings is essential yet underexplored in digital creation. Prior methods either generate from scratch or inpaint local gaps without predicting global structure, leading to coarse contours and limited detail. To address this, we introduce SketchRevive, a two‑stage framework for fine‑grained pixel‑to‑vector sketch completion that couples diffusion‑based pixel completion with MLLM‑driven refinement and vectorization to produce coherent, detail‑faithful SVG results. Specifically, we first construct a practical benchmark by augmenting stroke‑annotated sketches from paper and whiteboards. Stage I trains a diffusion model with a line‑distribution head to predict per‑pixel stroke presence, producing structural and appearance consistent completions. Stage II fine-tunes an MLLM for structure‑aware SVG vectorization with iterative refinement, optimized by instance‑level stroke attribute similarities. To align key clues e.g. spatial structure, appearance details across both stages, we introduce a diffusion-prior aggregated encoding module by injecting multi‑scale UNet features from Stage I into the MLLM’s visual embeddings and using line prediction logits for token compression to prioritize informative tokens. Experiments indicate that SketchRevive completes topology‑coherent vector outputs with high fidelity and recognizability while preserving user intent, suitable for interactive creation and artistic design.


---

## 33. Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision

> 🇯🇵 **Vanast：合成トリプレット教師ありの人間画像アニメーション仮想試着**

> 💡 人間画像アニメーションによる仮想試着システム。

**著者:** Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Cha_Vanast_Virtual_Try-On_with_Human_Image_Animation_via_Synthetic_Triplet_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2604.04934) | [🌐 Project](https://hyunsoocha.github.io/vanast/)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/39279.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://hyunsoocha.github.io/vanast/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** We present Vanast, a unified framework that generates garment-transferred human animation videos directly from a single human image, garment images, and a pose guidance video. Conventional two-stage pipelines treat image-based virtual try-on and pose-driven animation as separate processes, which often results in identity drift, garment distortion, and front–back inconsistency. Our model addresses these issues by performing the entire process in a single unified step to achieve coherent synthesis. To enable this setting, we construct large-scale triplet supervision.  Our data generation pipeline includes generating identity-preserving human images in alternative outfits that differ from garment catalog images, capturing full upper and lower garment triplets to overcome the single-garment–posed video pair limitation, and assembling diverse in-the-wild triplets without requiring garment catalog images. We further introduce a Dual Module architecture for video diffusion transformers to stabilize training, preserve pretrained generative quality, and improve garment accuracy, pose adherence, and identity preservation while supporting zero-shot garment interpolation. Together, these contributions allow Vanast to produce high-fidelity, identity-consistent animation across a wide range of garment types.


---

## 34. Feed-Forward One-Shot Animatable Textured Mesh Avatar Reconstruction

> 🇯🇵 **フィードフォワード単一ショット アニメーション化テクスチャメッシュアバター再構成**

> 💡 単一フレームからのアニメーション化テクスチャメッシュアバター再構成。

**著者:** Yisheng He

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/He_Feed-Forward_One-Shot_Animatable_Textured_Mesh_Avatar_Reconstruction_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2604.22865)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/39107.png)


**Abstract:** We introduce a feed-forward framework for one-shot animatable mesh head reconstruction that generates high-fidelity, directly animatable 3D head avatars from a single image. Unlike previous work that relies on time-consuming test-time optimization or extensive multi-view data, our method produces complete mesh representations with inherent animatability from a single image in a single forward pass. Our approach employs a dual shape and texture map architecture that simultaneously processes mesh vertices and texture map with extracted image features from a shared transformer backbone, allowing for coherent shape carving and appearance modeling. To prevent mesh collapse and ensure topological integrity during feed-forward deformation, we propose an iterative GRU-based decoding mechanism with progressive geometry deformation and texture refinement, coupled with a novel reprojection-based texture guidance mechanism that anchors appearance learning to the input image. Extensive experiments demonstrate that our method outperforms state-of-the-art approaches in reconstruction quality, animation capability, and computational efficiency. Code will be made publicly available.


---

## 35. ProgressiveAvatars: Progressive Animatable 3D Gaussian Avatars

> 🇯🇵 **ProgressiveAvatars：進行的アニメーション化3Dガウス分布アバター**

> 💡 進行的学習アプローチによるアニメーション化3Dガウス分布アバター。

**著者:** Kaiwen Song, Jinkai Cui, Juyong Zhang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Song_ProgressiveAvatars_Progressive_Animatable_3D_Gaussian_Avatars_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.16447)

**Session:** Poster Session 5 & Exhibit Hall


![Poster](posters/anime/36697.png)


**Abstract:** In practical real-time XR and telepresence applications, network and computing resources fluctuate frequently. Therefore, a progressive, streamable 3D representation method is needed that can be immediately deployed and continuously optimized as resources increase. To this end, we propose ProgressiveAvatars, a progressive avatar representation built on a hierarchy of 3D Gaussians grown byadaptive implicit subdivision on a template mesh. 3D Gaussians are defined in face‑local coordinates to remain animatable under varying expressions and head motion across multiple detail levels. The hierarchy expands when screen-space signals indicate a lack of detail, allocating resources to important areas. ProgressiveAvatars supports incremental loading rendering, adding new Gaussians as they arrive while preserving previous content, thus achieving smooth quality improvements across varying bandwidths. Thanks to our progressive representation method with an inherited tree structure, ProgressiveAvatars enables progressive delivery and progressive rendering under fluctuating network bandwidth and varying compute and memory resources.


---

## 36. SEA: Evaluating Sketch Abstraction Efficiency via Element-level Commonsense Visual Question Answering

> 🇯🇵 **SEA：要素レベル常識視覚質問応答によるスケッチ抽象化効率評価**

> 💡 スケッチの抽象化効率を視覚的推論で評価するフレームワーク。

**著者:** Jiho Park, Sieun Choi, Jaeyoon Seo, Minho Sohn, Yeana Kim, Jihie Kim

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Park_SEA_Evaluating_Sketch_Abstraction_Efficiency_via_Element-level_Commonsense_Visual_Question_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.28363)

**Session:** Poster Session 5 & Exhibit Hall


![Poster](posters/anime/37001.png)


**Abstract:** A sketch is a distilled form of visual abstraction that conveys core concepts through simplified yet purposeful strokes while omitting extraneous detail. Despite its expressive power, quantifying the efficiency of semantic abstraction in sketches remains challenging. Existing evaluation methods that rely on reference images, low-level visual features, or recognition accuracy do not capture abstraction, the defining property of sketches.To address these limitations, we introduce SEA (Sketch Evaluation metric for Abstraction efficiency), a reference-free metric that assesses how economically a sketch represents class-defining visual elements while preserving semantic recognizability. These elements are derived per class from commonsense knowledge about features typically depicted in sketches. SEA leverages a visual question answering model to determine the presence of each element and returns a quantitative score that reflects semantic retention under simple visual representations.To support this metric, we present CommonSketch, the first semantically annotated sketch dataset, comprising 23,100 human-drawn sketches across 300 classes, each paired with a caption and element-level annotations. Experiments show that SEA aligns closely with human judgments and reliably discriminates levels of abstraction efficiency, while CommonSketch serves as a benchmark providing systematic evaluation of element-level sketch understanding across various vision-language models.


---

## 37. Region-Wise Correspondence Prediction between Manga Line Art Images

> 🇯🇵 **漫画線画画像間の領域対応予測**

> 💡 漫画線画における領域単位の対応関係を予測し、高度な漫画理解・編集タスクを可能にするフレームワークを提案。

**著者:** Yingxuan Li, Jiafeng Mao, Qianru Qiu, Yusuke Matsui

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Region-Wise_Correspondence_Prediction_between_Manga_Line_Art_Images_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2509.09501)

**Session:** Poster Session 3 & Exhibit Hall


> 🚫 Poster image not yet available


**Abstract:** Understanding region-wise correspondences between manga line art images is fundamental for high-level manga processing, supporting downstream tasks such as line art colorization and in-between frame generation. Unlike natural images that contain rich visual cues, manga line art consists only of sparse black-and-white strokes, making it challenging to determine which regions correspond across images. In this work, we introduce a new task: predicting region-wise correspondence between raw manga line art images without any annotations. To address this problem, we propose a Transformer-based framework trained on large-scale, automatically generated region correspondences. The model learns to suppress noisy matches and strengthen consistent structural relationships, resulting in robust patch-level feature alignment within and across images. During inference, our method segments each line art and establishes coherent region-level correspondences through edge-aware clustering and region matching. We construct manually annotated benchmarks for evaluation, and experiments across multiple datasets demonstrate both high patch-level accuracy and strong region-level correspondence performance, achieving 78.4-84.4% region-level accuracy. These results highlight the potential of our method for real-world manga and animation applications.


---

## 38. DynamicTree: Interactive Real Tree Animation via Sparse Voxel Spectrum

> 🇯🇵 **DynamicTree：疎ボクセルスペクトラムによるインタラクティブなリアルタイム樹木アニメーション**

> 💡 疎ボクセルスペクトラムを利用した樹木ダイナミクスのリアルタイムアニメーション。

**著者:** Yaokun Li, Lihe Ding, Xiao Chen, Guang Tan, Tianfan Xue

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_DynamicTree_Interactive_Real_Tree_Animation_via_Sparse_Voxel_Spectrum_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2510.22213)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/36386.png)


**Abstract:** Generating dynamic and interactive 3D trees has wide applications in virtual reality, games, and world simulation. However, existing methods still face various challenges in generating structurally consistent and realistic 4D motion for complex real trees. In this paper, we propose DynamicTree, the first framework that can generate long-term, interactive 3D motion for 3DGS reconstructions of real trees. Unlike prior optimization-based methods, our approach generates dynamics in a fast feed-forward manner. The key success of our approach is the use of a compact sparse voxel spectrum to represent the tree movement. Given a 3D tree from Gaussian Splatting reconstruction, our pipeline first generates mesh motion using the sparse voxel spectrum and then binds Gaussians to deform the mesh. Additionally, the proposed sparse voxel spectrum can also serve as a basis for fast modal analysis under external forces, allowing real-time interactive responses. To train our model, we also introduce 4DTree, the first large-scale synthetic 4D tree dataset containing 8,786 animated tree meshes with semantic labels and 100-frame motion sequences. Extensive experiments demonstrate that our method achieves realistic and responsive tree animations, significantly outperforming existing approaches in both visual quality and computational efficiency.


---

## 39. SketchAssist: A Practical Assistant for Semantic Edits and Precise Local Redrawing

> 🇯🇵 **SketchAssist：セマンティック編集と精密な局所再描画実用支援ツール**

> 💡 セマンティック編集と精密な局所再描画をサポートするスケッチ支援ツール。

**著者:** Han Zou, Yan Zhang, Ruiqi Yu, Cong Xie, Jie Huang, Zhan Zhenpeng

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zou_SketchAssist_A_Practical_Assistant_for_Semantic_Edits_and_Precise_Local_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.14140)

**Session:** Poster Session 3 & Exhibit Hall


![Poster](posters/anime/38741.png)


**Abstract:** Sketch editing is central to digital illustration, yet existing image editing systems struggle to preserve the sparse, style‑sensitive structure of line art while supporting both high‑level semantic changes and precise local redrawing. We present SketchAssist, an interactive sketch drawing assistant that accelerates creation by unifying instruction‑guided global edits with line‑guided region redrawing, while keeping unrelated regions and overall composition intact. To enable this assistant at scale, we introduce a controllable data generation pipeline that (i) constructs attribute‑addition sequences from attribute‑free base sketches, (ii) forms multi‑step edit chains via cross‑sequence sampling, and (iii) expands stylistic coverage with a style‑preserving attribute‑removal model applied to diverse sketches. Building on this data, SketchAssist employs a unified sketch editing framework with minimal changes to DiT‑based editors. We repurpose the RGB channels to encode the inputs, enabling seamless switching between  instruction‑guided edits and line‑guided redrawing within a single input interface. To further specialize behavior across modes, we integrate a task‑guided mixture‑of‑experts into LoRA layers, routing by text and visual cues to improve semantic controllability, structural fidelity, and style preservation.Extensive experiments show state‑of‑the‑art results on both tasks, with superior instruction adherence and style/structure preservation compared to recent baselines. Together, our dataset and SketchAssist provide a practical, controllable assistant for sketch creation and revision


---

## 40. Let it Snow! Animating 3D Gaussian Scenes with Dynamic Weather Effects via Physics-Guided Score Distillation

> 🇯🇵 **Let it Snow!：物理誘導スコア蒸留によるダイナミック天候効果付き3Dガウスシーンアニメーション**

> 💡 物理ガイド付きスコア蒸留を使用した動的天候エフェクト付きシーンアニメーション。

**著者:** Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Fiebelman_Let_it_Snow_Animating_3D_Gaussian_Scenes_with_Dynamic_Weather_CVPR_2026_paper.html) | [🌐 Project](https://galfiebelman.github.io/let-it-snow/)

**Session:** Poster Session 6


![Poster](posters/anime/37114.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://galfiebelman.github.io/let-it-snow/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** 3D Gaussian Splatting has recently enabled fast and photorealistic reconstruction of static 3D scenes. However, dynamic editing of such scenes remains a significant challenge. We introduce a novel framework, Physics-Guided Score Distillation, to address a fundamental conflict: physics simulation provides a strong motion prior that is insufficient for photorealism , while video-based Score Distillation Sampling (SDS) alone cannot generate coherent motion for complex, multi-particle scenarios. We resolve this through a unified optimization framework where physics simulation guides Score Distillation to jointly refine the motion prior for photorealism while simultaneously optimizing appearance. Specifically, we learn a neural dynamics model that predicts particle motion and appearance, optimized end-to-end via a combined loss integrating Video-SDS for photorealism with our physics-guidance prior. This allows for photorealistic refinements while ensuring the dynamics remain plausible. Our framework enables scene-wide dynamic weather effects, including snowfall, rainfall, fog, and sandstorms, with physically plausible motion. Experiments demonstrate our physics-guided approach significantly outperforms baselines, with ablations confirming this joint refinement is essential for generating coherent, high-fidelity dynamics.


---

## 41. Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling

> 🇯🇵 **Ani3DHuman：自己誘導確率的サンプリングによるフォトリアリスティック3D人間アニメーション**

> 💡 自己誘導確率的サンプリングによるフォトリアリスティック3D人間アニメーション。

**著者:** Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_Ani3DHuman_Photorealistic_3D_Human_Animation_with_Self-guided_Stochastic_Sampling_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2602.19089) | [🌐 Project](https://github.com/qiisun/ani3dhuman)

**Session:** Poster Session 2 & Exhibit Hall w/ Coffee Break


![Poster](posters/anime/38317.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://github.com/qiisun/ani3dhuman" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Current 3D human animation methods fail at photorealism: kinematics-based approaches lack non-rigid dynamics like clothing, while methods reconstructing from generated videos suffer from low-quality artifacts and identity loss. To overcome these limitations, we present Ani3DHuman, a framework that marries kinematics-based animation with video diffusion priors. We first introduce a layered motion representation that disentangles rigid motion and residual non-rigid motion. Then, we use a pretrained video diffusion model to restore a coarse rendering from the mesh-rigged animation, which provides supervision for the motion field. However, this restoration task, based on diffusion sampling, is highly challenging, as the initial renderings are out-of-distribution, causing standard deterministic ODE samplers to fail. Therefore, our core technical contribution is self-guided stochastic sampling, which effectively solves the out-of-distribution problem by combining stochastic sampling (for photorealistic quality) with self-guidance (for identity fidelity). These restored videos provide high-quality supervision, enabling the optimization of a realistic 4D motion field. Ani3DHuman achieves state-of-the-art results, and our ablations validate that both components of our sampler are essential for high-fidelity restoration.


---

## 42. SketchFaceGS: Real-Time Sketch-Driven Face Editing and Generation with Gaussian Splatting

> 🇯🇵 **SketchFaceGS：ガウス スプラッティングによるリアルタイムスケッチ駆動顔編集・生成**

> 💡 スケッチ条件付きリアルタイム顔編集・生成フレームワーク。

**著者:** Bo Li, Jiahao Kang, Yubo Ma, Feng-Lin Liu, Bin Liu, Fang-Lue Zhang, Lin Gao

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_SketchFaceGS_Real-Time_Sketch-Driven_Face_Editing_and_Generation_with_Gaussian_Splatting_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2604.19202)

**Session:** Poster Session 6


![Poster](posters/anime/36480.png)


**Abstract:** 3D Gaussian representations have emerged as a powerful paradigm for digital head modeling, achieving photorealistic quality with real-time rendering. However, intuitive and interactive creation or editing of 3D Gaussian head models remains challenging. Although 2D sketches provide an ideal interaction modality for fast, intuitive conceptual design, they are sparse, depth-ambiguous, and lack high-frequency appearance cues, making it difficult to infer dense, geometrically consistent 3D Gaussian structures from strokes—especially under real-time constraints. To address these challenges, we propose SketchFaceGS, the first sketch-driven framework for real-time generation and editing of photorealistic 3D Gaussian head models from 2D sketches. Our method uses a feed-forward, coarse-to-fine architecture. A Transformer-based UV feature-prediction module first reconstructs a coarse but geometrically consistent UV feature map from the input sketch, and a 3D UV feature enhancement module refines it with high-frequency, photorealistic detail to produce a high-fidelity 3D head. For editing, we introduce a UV Mask Fusion technique combined with a layer-by-layer feature-fusion strategy, enabling precise, real-time, free-viewpoint modifications. Extensive experiments show that SketchFaceGS outperforms existing methods in both generation fidelity and editing flexibility, producing high-quality, editable 3D heads from sketches in a single forward pass.


---

## 43. Sketch2Colab: Sketch-Conditioned Multi-Human Animation via Controllable Flow Distillation

> 🇯🇵 **Sketch2Colab：制御可能フロー蒸留による複数人間アニメーションスケッチ条件化**

> 💡 スケッチ条件付きの制御可能な複数人間アニメーション生成。

**著者:** Divyanshu Daiya, Aniket Bera

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Daiya_Sketch2Colab_Sketch-Conditioned_Multi-Human_Animation_via_Controllable_Flow_Distillation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.02190)

**Session:** Poster Session 5 & Exhibit Hall


![Poster](posters/anime/36994.png)


**Abstract:** We present \emph{Sketch2Colab}, which turns storyboard-style 2D sketches into coherent, object-aware 3D multi-human motion with fine-grained control over agents, joints, timing, and contacts. Conventional diffusion-based motion generators have advanced realism; however, achieving precise adherence to rich interaction constraints typically demands extensive training and/or costly posterior guidance, and performance can degrade under strong multi-entity conditioning. Sketch2Colab instead first learns a sketch-driven diffusion prior and then distills it into an efficient rectified-flow student operating in latent space for fast, stable sampling. Differentiable energies over keyframes, trajectories, and physics-based constraints directly shape the student’s transport field, steering samples toward motions that faithfully satisfy the storyboard while remaining physically plausible. To capture coordinated interaction, we augment the continuous flow with a continuous-time Markov chain (CTMC) planner that schedules discrete events such as touches, grasps, and handoffs, modulating the dynamics to produce crisp, well-phased human–object–human collaborations. Experiments on CORE4D and InterHuman show that Sketch2Colab achieves state-of-the-art constraint adherence and perceptual quality while offering significantly faster inference than diffusion-only baselines.


---

## 44. ActionMesh: Animated 3D Mesh Generation with Temporal 3D Diffusion

> 🇯🇵 **ActionMesh：時間的3D拡散によるアニメーション3Dメッシュ生成**

> 💡 時間的3D拡散モデルを使用したアニメーション3Dメッシュ生成。

**著者:** Remy Sabathier, David Novotny, Niloy J. Mitra, Tom Monnier

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Sabathier_ActionMesh_Animated_3D_Mesh_Generation_with_Temporal_3D_Diffusion_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2601.16148) | [🌐 Project](https://remysabathier.github.io/actionmesh/)

**Session:** Poster Session 5 & Exhibit Hall


> 🚫 Poster image not yet available


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://remysabathier.github.io/actionmesh/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Generating animated 3D objects is at the heart of many applications, yet most advanced works are typically difficult to apply in practice because of their limited setup, their long runtime, or their limited quality. We introduce ActionMesh, a generative model that predicts production-ready 3D meshes "in action" in a feed-forward manner. Drawing inspiration from early video models, our key insight is to modify existing 3D diffusion models to include a temporal axis, resulting in a framework we dubbed "temporal 3D diffusion". Specifically, we first adapt the 3D diffusion stage to generate a sequence of synchronized latents representing time-varying and independent 3D shapes. Second, we design a temporal 3D autoencoder that translates a sequence of independent shapes into the corresponding deformations of a pre-defined reference shape, allowing us to build an animation. Combining these two components, ActionMesh generates animated 3D meshes from different inputs like a monocular video, a text description, or even a 3D mesh with a text prompt describing its animation. Besides, compared to previous approaches, our method is fast and produces results that are rig-free and topology consistent, hence enabling rapid iteration and seamless applications like texturing and retargeting. We evaluate our model on standard video-to-4D benchmarks (Consistent4D, Objaverse) and report state-of-the-art performances on both geometric accuracy and temporal consistency, demonstrating that our model can deliver animated 3D meshes with unprecedented speed and quality.


---

## 45. SketchDeco: Training-Free Latent Composition for Precise Sketch Colourisation

> 🇯🇵 **SketchDeco：精密スケッチ色付けのための訓練フリー潜在空間合成**

> 💡 マスクと色パレットを使用した精密なスケッチ色付けのための訓練フリーアプローチ。

**著者:** Chaitat Utintu, Yi-Zhe Song

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Utintu_SketchDeco_Training-Free_Latent_Composition_for_Precise_Sketch_Colourisation_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2405.18716) | [🌐 Project](https://chaitron.github.io/SketchDeco/)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/36458.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://chaitron.github.io/SketchDeco/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** We introduce SketchDeco, a training-free approach to sketch colourisation that bridges the gap between professional design needs and intuitive, region-based control. Our method empowers artists to use simple masks and colour palettes for precise spatial and chromatic specification, avoiding both the tediousness of manual assignment and the ambiguity of text-based prompts. We reformulate this task as a novel, training-free composition problem. Our core technical contribution is a guided latent-space blending process: we first leverage diffusion inversion to precisely ``paint'' user-defined colours into specified regions, and then use a custom self-attention mechanism to harmoniously blend these local edits with a globally consistent base image. This ensures both local colour fidelity and global harmony without requiring any model fine-tuning. Our system produces high-quality results in 15--20 inference steps on consumer GPUs, making professional-quality, controllable colourisation accessible.


---

## 46. EmoStyle: Emotion-Driven Image Stylization

> 🇯🇵 **EmoStyle：感情駆動画像スタイライゼーション**

> 💡 特定の感情を喚起しながらコンテンツを保存する感情駆動スタイライゼーション。

**著者:** Jingyuan Yang, Zihuan Bai, Hui Huang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yang_EmoStyle_Emotion-Driven_Image_Stylization_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.05478)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/38594.png)


**Abstract:** Art has long been a profound medium for expressing emotions.While existing image stylization methods effectively transform visual appearance, they often overlook the emotional impact carried by styles.To bridge this gap, we introduce Affective Image Stylization (AIS), a task that applies artistic styles to evoke specific emotions while preserving content.We present EmoStyle, a framework designed to address key challenges in AIS, including the lack of training data and the emotion–style mapping.First, we construct EmoStyleSet, a content-emotion-stylized image triplet dataset derived from ArtEmis to support AIS.We then propose an Emotion–Content Reasoner that adaptively integrates emotional cues with content to learn coherent style queries.Given the discrete nature of artistic styles, we further develop a Style Quantizer that converts continuous style features into emotion-related codebook entries.Extensive qualitative and quantitative evaluations, including user studies, demonstrate that EmoStyle enhances emotional expressiveness while maintaining content consistency.Moreover, the learned emotion-aware style dictionary is adaptable to other generative tasks, highlighting its potential for broader applications.Our work establishes a foundation for emotion-driven image stylization, expanding the creative potential of AI-generated art.


---

## 47. Bidirectional Query-Driven Generation of Parametric CAD Sketch

> 🇯🇵 **双方向クエリ駆動パラメトリック CAD スケッチ生成**

> 💡 CAD プロセスの非線形構築ロジックを内部化した、パラメトリックスケッチ完成フレームワーク。

**著者:** Yang Liu, Daxuan Ren, Yijie Ding, Jianmin Zheng, Fang Deng

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_Bidirectional_Query-Driven_Generation_of_Parametric_CAD_Sketch_CVPR_2026_paper.html)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/39199.png)


**Abstract:** Learning-based CAD modeling shows great promise in automating parametric design, yet existing approaches often overlook the incremental and state-dependent nature of sketch construction. We present CADSketcher, a query-driven bidirectional framework for completing partial parametric sketches by internalizing the non-linear construction logic of interactive CAD processes. At the core of CADSketcher are two key innovations. First, a bidirectional sketch learner recovers both prior and posterior contexts from arbitrary-span partial sketches via a bidirectional query mechanism, enabling exploration of multiple plausible modeling trajectories. Second, a confidence-guided completion pipeline adaptively determines the expansion direction through a confidence gate and ensures executable instruction generation using a validity compiler, while a progressive context updater preserves sketch consistency throughout the evolving sketch state. In addition, a hybrid positional encoding integrates global modeling progression with local geometric semantics, reinforcing structural coherence during both learning and completion. Extensive experiments demonstrate that CADSketcher achieves superior geometric validity and instruction consistency across diverse sketch completion tasks, offering a robust and interpretable framework toward intelligent CAD automation.


---

## 48. Soul: Breathe Life into Digital Human for High-fidelity Long-term Multimodal Animation

> 🇯🇵 **Soul：高忠実度長期マルチモーダルアニメーションのデジタル人間に生命を吹き込む**

> 💡 単一フレーム画像・テキスト・音声から長期のセマンティック一貫性ビデオを生成。

**著者:** Jiangning Zhang, junwei zhu, Zhenye Gan, Donghao Luo, Chuming Lin, FeiFan Xu, Xu Peng, Jianlong Hu, Yuansen Liu, Yijia Hong, Weijian Cao, Han Feng, Xu Chen, Chencan Fu, Keke He, Xiaobin Hu, Chengjie Wang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_Soul_Breathe_Life_into_Digital_Human_for_High-fidelity_Long-term_Multimodal_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2512.13495)

**Session:** Poster Session 1 & Exhibit Hall


> 🚫 Poster image not yet available


**Abstract:** We propose a multimodal-driven framework for high-fidelity long-term digital human animation termed Soul, which generates semantically coherent videos from a single-frame portrait image, text prompts, and audio, achieving precise lip synchronization, vivid facial expressions, and robust identity preservation. We construct Soul-1M, containing 1 million finely annotated samples with a precise automated annotation pipeline (covering portrait, upper-body, full-body, and multi-person scenes) to mitigate data scarcity, and we carefully curate Soul-Bench for comprehensive and fair evaluation of audio-/text-guided animation methods. The model is built on the Wan2.2-5B backbone, integrating audio-injection layers and multiple training strategies together with threshold-aware codebook replacement to ensure long-term generation consistency. Meanwhile, step/CFG distillation and a lightweight VAE are used to optimize inference efficiency, achieving an 11.4$\times$ speedup with negligible quality loss. Extensive experiments show that Soul significantly outperforms current leading open-source and commercial models on video quality, video–text alignment, identity preservation, and lip-synchronization accuracy, demonstrating broad applicability in real-world scenarios such as virtual anchors and film production.


---

## 49. InfinityHuman: Towards Long-Term Audio-Driven Human Animation

> 🇯🇵 **InfinityHuman：長期音声駆動人間アニメーションへ向けて**

> 💡 ポーズガイド付きリファイナーで長期間の高解像度ビデオを生成する粗から細へのフレームワーク。

**著者:** Xiaodi Li, Pan Xie, Yi Ren, Qijun Gan, Chen Zhang, Fangyuan Kong, Xiang Yin, Zehuan Yuan, BINGYUE PENG

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Li_InfinityHuman_Towards_Long-Term_Audio-Driven_Human_Animation_CVPR_2026_paper.html)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/40229.png)


**Abstract:** Audio-driven human animation has attracted wide attention thanks to its practical applications. However, critical challenges remain in generating high-resolution, long-duration videos with consistent appearance and natural hand motions. Existing methods extend videos using overlapping motion frames but suffer from error accumulation, leading to identity drift, color shifts, and scene instability. Additionally, hand movements are poorly modeled, resulting in noticeable distortions and misalignment with the audio. In this work, we propose InfinityHuman, a coarse-to-fine framework that first generates audio-synchronized representations, then progressively refines them into high-resolution, long-duration videos using a pose-guided refiner. Since pose sequences are decoupled from appearance and resist temporal degradation, our pose-guided refiner employs stable poses and the initial frame as a visual anchor to reduce drift and improve lip synchronization. Moreover, to enhance semantic accuracy and gesture realism, we introduce a hand-specific reward mechanism trained with high-quality hand motion data. Experiments on the EMTD and HDTF datasets show that InfinityHuman achieves state-of-the-art performance in video quality, identity preservation, hand accuracy, and lip-sync. Ablation studies further confirm the effectiveness of each module.


---

## 50. One-to-All Animation: Alignment-Free Character Animation and Image Pose Transfer

> 🇯🇵 **One-to-All Animation：配置フリーキャラクターアニメーションと画像ポーズ転送**

> 💡 参照ポーズのミスアライメント処理に対応した統合キャラクターアニメーション。

**著者:** Shijun Shi, Jing Xu, Zhihang Li, Chunli Peng, Xiaoda Yang, Lijing Lu, Kai Hu, Jiangning Zhang

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_One-to-All_Animation_Alignment-Free_Character_Animation_and_Image_Pose_Transfer_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2511.22940) | [🌐 Project](https://ssj9596.github.io/one-to-all-animation-project/)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/38503.png)


<details>
<summary>🌐 Project Page プレビュー</summary>

<iframe src="https://ssj9596.github.io/one-to-all-animation-project/" width="100%" height="600" loading="lazy" style="border:none;"></iframe>

</details>


**Abstract:** Recent advances in diffusion models have greatly improved pose-driven character animation. However, existing methods are limited to spatially aligned reference-pose pairs with matched skeletal structures. Handling reference-pose misalignment remains unsolved. To address this, we present One-to-All Animation, a unified framework for high-fidelity character animation and image pose transfer for references with arbitrary layouts. First, to handle spatially misaligned reference, we reformulate training as a self-supervised outpainting task that transforms diverse-layout reference into a unified occluded-input format. Second, to process partially visible reference, we design a reference extractor for comprehensive identity feature extraction. Further, we integrate hybrid reference fusion attention to handle varying resolutions and dynamic sequence lengths. Finally, from the perspective of generation quality, we introduce identity-robust pose control that decouples appearance from skeletal structure to mitigate pose overfitting, and a token replace strategy for coherent long-video generation. Extensive experiments show that our method outperforms existing approaches. The code and model will be available.


---

## 51. Tavatar: Topology-Aware Gaussian Attribute Derivation for Animatable Human Avatars

> 🇯🇵 **Tavatar：トポロジー認識ガウス属性導出アニメーション化人間アバター**

> 💡 ローカルメッシュ幾何学からガウス属性を解析的に導出する堅牢なアニメーション手法。

**著者:** Hailin Luo, Yifan Yang, Jiazhi Shu, Zixiong Huang, Qi Chen, Qing Du, Mingkui Tan

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Luo_Tavatar_Topology-Aware_Gaussian_Attribute_Derivation_for_Animatable_Human_Avatars_CVPR_2026_paper.html)

**Session:** Poster Session 1 & Exhibit Hall


![Poster](posters/anime/39602.png)


**Abstract:** Reconstructing high-fidelity, animatable human avatars from monocular videos remains a critical challenge. Existing 3DGS-based human animation methods constrain Gaussian parameters but exclude scale, which we argue is crucial for adapting human poses to challenging out-of-distribution poses. To achieve robust animation under unseen poses, we propose Tavatar, which derives key parameters such as scale, rotation, and other geometric attributes directly from the local mesh geometry, instead of learning them through unconstrained optimization. This paradigm shift enforces topological consistency by design, as each Gaussian is analytically anchored to the local mesh geometry, inheriting its spatial structure and deformation behavior. Specifically, we bind Gaussians to mesh faces and vertices, deriving their scales and orientations from triangle properties and local edge lengths to ensure coherent surface coverage. To ensure the stability of this analytical mapping, we introduce a crucial equilateral regularization term that preserves mesh integrity. Extensive experiments demonstrate that Tavatar achieves superior animation robustness on challenging out-of-distribution poses, reducing normal error by 13.8\% on X-Avatar and 17.9\% on PeopleSnapshot against the best baseline, while maintaining competitive rendering quality.


---

## 52. SketchVL: Policy Optimization via Fine-Grained Credit Assignment for Chart Understanding and More

> 🇯🇵 **SketchVL：チャート理解とその先へのきめ細かい信用割り当てによるポリシー最適化**

> 💡 ステップレベルでの推論品質を評価できるマルチモーダル大規模言語モデル。

**著者:** Muye Huang, Lingling Zhang, Yifei Li, Yaqiang Wu, Jun Liu

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Huang_SketchVL_Policy_Optimization_via_Fine-Grained_Credit_Assignment_for_Chart_Understanding_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2601.05688)

**Session:** Poster Session 1 & Exhibit Hall


> 🚫 Poster image not yet available


**Abstract:** Charts are high-density visual carriers of complex data and medium for information extraction and analysis. Due to the need for precise and complex visual reasoning, automated chart understanding poses a significant challenge to existing Multimodal Large Language Models (MLLMs). Many MLLMs trained with reinforcement learning (RL) face the challenge of credit assignment. Their advantage estimation, typically performed at the trajectory level, cannot distinguish between correct and incorrect reasoning steps within a single generated response. To address this limitation, we introduce SketchVL, a novel MLLM that optimized with FinePO, a new RL algorithm designed for fine-grained credit assignment within each trajectory. SketchVL's methodology involves drawing its intermediate reasoning steps as markers on the image and feeding the annotated image back to itself, creating a robust, multi-step reasoning process. During training, the FinePO algorithm leverages a Fine-grained Process Reward Model (FinePRM) to score each drawing action within a trajectory, thereby precisely assigning credit for each step. This mechanism allows FinePO to more strongly reward correct tokens when a trajectory is globally successful, and more heavily penalize incorrect tokens when the trajectory is globally suboptimal, thus achieving fine-grained reinforcement signals. Experiments show that SketchVL learns to align its step-level behavior with the FinePRM, achieving an average performance gain of 7.23\% over its base model across chart datasets, natural image datasets, and mathematics, providing a promising new direction for training powerful reasoning models.


---

## 53. MultiAnimate: Pose-Guided Image Animation Made Extensible

> 🇯🇵 **MultiAnimate：拡張性を実現したポーズ誘導画像アニメーション**

> 💡 複数キャラクター間の配置関係を捉えるディフュージョン変換器ベースのアニメーション。

**著者:** Yingcheng Hu, Haowen Gong, Chuanguang Yang, Zhulin An, Yongjun Xu, Songhua Liu

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Hu_MultiAnimate_Pose-Guided_Image_Animation_Made_Extensible_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2602.21581)

**Session:** Poster Session 2 & Exhibit Hall w/ Coffee Break


![Poster](posters/anime/39873.png)


**Abstract:** Pose-guided human image animation aims to synthesize realistic videos of a reference character driven by a sequence of poses. While diffusion-based methods have achieved remarkable success, most existing approaches are limited to single-character animation. We observe that naively extending these methods to multi-character scenarios often leads to identity confusion and implausible occlusions between characters. To address these challenges, in this paper, we propose an extensible multi-character image animation framework built upon modern Diffusion Transformers (DiTs) for video generation. At its core, our framework introduces two novel components—Identifier Assigner and Identifier Adapter—which collaboratively capture per-person positional cues and inter-person spatial relationships. This mask-driven scheme, along with a scalable training strategy, not only enhances flexibility but also enables generalization to scenarios with more characters than those seen during training. Remarkably, trained on only a two-character dataset, our model generalizes to multi-character animation while maintaining compatibility with single-character cases. Extensive experiments demonstrate that our approach achieves state-of-the-art performance in multi-character image animation, surpassing existing diffusion-based baselines. Codes will be released.


---

## 54. Towards High-resolution and Disentangled Reference-based Sketch Colorization

> 🇯🇵 **高解像度分離参照ベーススケッチ色付けへ向けて**

> 💡 SDXL バックボーンとタガーネットワークを使用した高解像度で分離されたスケッチ色付け。

**著者:** Dingkun Yan, Xinrui Wang, Ru Wang, Zhuoru Li, Jinze Yu, Yusuke Iwasawa, Yutaka Matsuo, Jiaxian Guo

**Links:** [📄 Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Yan_Towards_High-resolution_and_Disentangled_Reference-based_Sketch_Colorization_CVPR_2026_paper.html) | [📋 arXiv](https://arxiv.org/abs/2603.05971)

**Session:** Poster Session 2 & Exhibit Hall w/ Coffee Break


> 🚫 Poster image not yet available


**Abstract:** Sketch colorization models have been widely studied to automate and assist in the creation of animation frames and digital illustrations. However, current methods are still not satisfactory for industrial standard applications in high-resolution synthesis and precise controllability of details. To further enhance the synthesis quality and controllability, we propose an image-referenced sketch colorization method based on the powerful SDXL backbone and leverage sketches as spatial guidance and RGB images as color references. A split cross-attention mechanism is coupled with spatial masks to separately colorize the foreground and background regions to avoid spatial entanglement. A tagger network trained on a massive anime-style image dataset is employed to extract attribution-level information from reference images and integrated into the pipeline to provide precise control signals for synthesis. However, the increased resolution and number of attention layers in the SDXL backbone and precise reference information from the tagger network cause severe entanglement during colorization. We consequently combine a foreground encoder and a background encoder for disentanglement and better synthesis quality. Furthermore, a high-quality annotated and paired sketch colorization dataset is collected for fine-tuning. The proposed method is the first to achieve high resolution high quality sketch colorization with precise control, and obvious outperforms existing methods in quantitative and qualitative validations, as well as user studies in both quality and controllability. Ablation study reveals the influence of each component. Code and dataset will be made publicly available upon paper acceptance.


---
