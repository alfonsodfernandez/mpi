export interface UserInfo {
  id: number;
  username: string;
  display_name: string;
  role: "student" | "admin";
  session_id: string;
}

export interface ProtectedCanvasSpec {
  kind: "matrix" | "augmented_matrix" | "text_lines";
  label: string;
  rows?: string[][];
  left?: string[][];
  right?: string[];
  lines?: string[];
}

export interface InputFieldSpec {
  id: string;
  label: string;
  type: "number" | "choice" | "vector";
  placeholder?: string;
  labels?: string[];
  options?: { value: string; label: string }[];
}

export interface InputSpec {
  kind: "number" | "vector" | "matrix" | "choice" | "multi_tf" | "multi_field";
  label?: string;
  placeholder?: string;
  labels?: string[];
  rows?: number;
  cols?: number;
  options?: { value: string; label: string }[];
  items?: { id: string; text: string }[];
  fields?: InputFieldSpec[];
}

export interface ExercisePrompt {
  statement_md: string;
  input_spec: InputSpec;
  protected_canvas?: ProtectedCanvasSpec | null;
  code_block?: string | null;
}

export interface PublicExercise {
  attempt_id: string;
  topic: string;
  topic_label: string;
  generator_id: string;
  title: string;
  difficulty: string;
  time_limit_seconds: number;
  started_at: string;
  expires_at: string;
  prompt: ExercisePrompt;
  watermark_text: string;
}

export interface ExerciseFeedback {
  attempt_id: string;
  status: string;
  is_correct: boolean;
  score: number;
  time_spent_seconds: number;
  feedback: string;
  correct_display: string;
  steps_md: string[];
  theory_ref: string;
}

export interface ExamQuestionPublic {
  question_id: string;
  question_index: number;
  topic: string;
  topic_label: string;
  title: string;
  points_weight: number;
  prompt: ExercisePrompt;
  answered: boolean;
  saved_answer: unknown;
}

export interface ActiveExam {
  exam_id: string;
  mode: string;
  title: string;
  total_questions: number;
  time_limit_seconds: number;
  started_at: string;
  expires_at: string;
  watermark_text: string;
  questions: ExamQuestionPublic[];
}

export interface ExamQuestionReview {
  question_id: string;
  question_index: number;
  topic: string;
  topic_label: string;
  title: string;
  points_weight: number;
  points_earned: number;
  is_correct: boolean;
  user_answer: unknown;
  correct_display: string;
  feedback: string;
  steps_md: string[];
  theory_ref: string;
  prompt: ExercisePrompt;
}

export interface ExamResult {
  exam_id: string;
  mode: string;
  title: string;
  status: string;
  score_10: number;
  correct_count: number;
  total_questions: number;
  time_spent_seconds: number;
  questions: ExamQuestionReview[];
}

export interface LogisticsNodeMetric {
  code: string;
  name: string;
  type: string;
  x: number;
  y: number;
  in_flow: number;
  out_flow: number;
  total_volume: number;
  in_degree: number;
  out_degree: number;
  total_degree: number;
  markov_pct: number;
  pagerank_pct: number;
  betweenness: number;
  norm_volume: number;
  norm_degree: number;
  norm_pagerank: number;
  norm_betweenness: number;
  is_isolated: boolean;
  is_dangling: boolean;
  rank_now: number;
  rank_before: number;
  rank_delta: number;
}

export interface LogisticsAnalysis {
  disabled_center: string | null;
  centers_all: { code: string; name: string; type: string; x: number; y: number }[];
  nodes: LogisticsNodeMetric[];
  ranking_pagerank: LogisticsNodeMetric[];
  active_flows: { source: string; target: string; flow: number }[];
  removed_flows: { source: string; target: string; flow: number }[];
  summary: {
    active_centers_count: number;
    active_routes_count: number;
    removed_routes_count: number;
    total_weekly_tonnes: number;
    lost_weekly_tonnes: number;
    pagerank_residual: number;
  };
  markov_methods: { method: string; iterations: number; residual_norm: number }[];
  demand: {
    historical: { year: number; volume: number }[];
    models: {
      degree: number;
      coefficients: number[];
      rmse: number;
      prediction_2028: number;
      pct_increase_vs_2025: number;
      fitted_series: number[];
    }[];
  };
}
